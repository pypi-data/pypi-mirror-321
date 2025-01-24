"""Module containing the app for the Numerous app."""

import asyncio
import inspect
import json
import logging
import uuid
from collections.abc import Callable
from dataclasses import dataclass, field
from inspect import getmembers
from pathlib import Path
from typing import Any

import jinja2
from anywidget import AnyWidget
from fastapi import HTTPException, Request, WebSocket
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from jinja2 import FileSystemLoader, meta
from starlette.responses import HTMLResponse
from starlette.websockets import WebSocketDisconnect

from .builtins import ParentVisibility
from .execution import _describe_widgets
from .models import (
    ActionRequestMessage,
    ActionResponseMessage,
    AppDescription,
    AppInfo,
    ErrorMessage,
    InitConfigMessage,
    MessageType,
    SetTraitValue,
    TemplateDescription,
    TraitValue,
    WidgetUpdateMessage,
    WidgetUpdateRequestMessage,
    encode_model,
)
from .server import (
    NumerousApp,
    SessionData,
    _get_session,
    _get_template,
    _load_main_js,
)


class AppProcessError(Exception):
    pass


# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

_app = NumerousApp()

# Get the base directory
BASE_DIR = Path.cwd()

# Add package directory setup near the top of the file
PACKAGE_DIR = Path(__file__).parent

# Configure templates with custom environment
templates = Jinja2Templates(
    directory=[str(BASE_DIR / "templates"), str(PACKAGE_DIR / "templates")]
)
templates.env.autoescape = False  # Disable autoescaping globally


@dataclass
class NumerousAppServerState:
    dev: bool
    main_js: str
    base_dir: str
    module_path: str
    template: str
    internal_templates: dict[str, str]
    sessions: dict[str, SessionData]
    connections: dict[str, dict[str, WebSocket]]
    widgets: dict[str, AnyWidget] = field(default_factory=dict)
    allow_threaded: bool = False


def wrap_html(key: str) -> str:
    return f'<div id="{key}"></div>'


def _handle_template_error(error_title: str, error_message: str) -> HTMLResponse:
    return HTMLResponse(
        content=templates.get_template("error.html.j2").render(
            {"error_title": error_title, "error_message": error_message}
        ),
        status_code=500,
    )


@_app.get("/")  # type: ignore[misc]
async def home(request: Request) -> Response:
    template = _app.state.config.template
    template_name = _get_template(template, _app.state.config.internal_templates)

    # Create the template context with widget divs
    template_widgets = {key: wrap_html(key) for key in _app.widgets}

    try:
        # Get template source and find undefined variables
        template_source = ""
        if isinstance(templates.env.loader, FileSystemLoader):
            template_source = templates.env.loader.get_source(
                templates.env, template_name
            )[0]
    except jinja2.exceptions.TemplateNotFound as e:
        return _handle_template_error("Template Error", f"Template not found: {e!s}")

    parsed_content = templates.env.parse(template_source)
    undefined_vars = meta.find_undeclared_variables(parsed_content)

    # Remove request and title from undefined vars as they are always provided
    undefined_vars.discard("request")
    undefined_vars.discard("title")

    # Check for variables in template that don't correspond to widgets
    unknown_vars = undefined_vars - set(template_widgets.keys())
    if unknown_vars:
        error_message = f"Template contains undefined variables that don't match\
            any widgets: {', '.join(unknown_vars)}"
        logger.error(error_message)
        return _handle_template_error("Template Error", error_message)

    # Rest of the existing code...
    template_content = templates.get_template(template_name).render(
        {"request": request, "title": "Home Page", **template_widgets}
    )

    # Check for missing widgets
    missing_widgets = [
        widget_id
        for widget_id in _app.widgets
        if f'id="{widget_id}"' not in template_content
    ]

    if missing_widgets:
        logger.warning(
            f"Template is missing placeholders for the following widgets:\
                {', '.join(missing_widgets)}. "
            "These widgets will not be displayed."
        )

    # Load the error modal template
    error_modal = templates.get_template("error_modal.html.j2").render()

    # Modify the template content to include the error modal
    modified_html = template_content.replace(
        "</body>", f'{error_modal}<script src="/numerous.js"></script></body>'
    )

    return HTMLResponse(content=modified_html)


@_app.get("/api/widgets")  # type: ignore[misc]
async def get_widgets(request: Request) -> dict[str, Any]:
    session_id = request.query_params.get("session_id")
    if session_id in {"undefined", "null", None}:
        session_id = str(uuid.uuid4())
    logger.info(f"Session ID: {session_id}")

    _session = _get_session(
        _app.state.config.allow_threaded,
        session_id,
        _app.state.config.base_dir,
        _app.state.config.module_path,
        _app.state.config.template,
        _app.state.config.sessions,
        load_config=True,
    )

    _app_definition: dict[str, Any] | InitConfigMessage = _session["config"]

    app_definition: InitConfigMessage
    # Convert to InitConfigMessage if it's not already
    if isinstance(_app_definition, dict):
        app_definition = InitConfigMessage(**_app_definition)
    else:
        app_definition = _app_definition

    return {
        "session_id": session_id,
        "widgets": app_definition.widget_configs,
        "logLevel": "DEBUG" if _app.state.config.dev else "ERROR",
    }


@_app.websocket("/ws/{client_id}/{session_id}")  # type: ignore[misc]
async def websocket_endpoint(
    websocket: WebSocket, client_id: str, session_id: str
) -> None:
    await websocket.accept()
    logger.debug(f"New WebSocket connection from client {client_id}")

    if session_id not in _app.state.config.connections:
        _app.state.config.connections[session_id] = {}

    _app.state.config.connections[session_id][client_id] = websocket

    session = _get_session(
        _app.state.config.allow_threaded,
        session_id,
        _app.state.config.base_dir,
        _app.state.config.module_path,
        _app.state.config.template,
        _app.state.config.sessions,
    )

    async def receive_messages() -> None:
        try:
            while True:
                await handle_receive_message(websocket, client_id, session)
        except (asyncio.CancelledError, WebSocketDisconnect):
            logger.debug(f"Receive task cancelled for client {client_id}")
            raise

    async def send_messages() -> None:
        try:
            while True:
                await handle_send_message(client_id, session)
        except (asyncio.CancelledError, WebSocketDisconnect):
            logger.debug(f"Send task cancelled for client {client_id}")
            raise

    try:
        await asyncio.gather(receive_messages(), send_messages())
    except (asyncio.CancelledError, WebSocketDisconnect):
        logger.debug(f"WebSocket tasks cancelled for client {client_id}")
    finally:
        cleanup_connection(session_id, client_id)


async def handle_receive_message(
    websocket: WebSocket, client_id: str, session: SessionData
) -> None:
    message = await websocket.receive_json()

    # First check if we have a message type
    message_type = message.get("type")

    if message_type in ["get-state", "get-widget-states"]:
        # These messages don't need widget_id, just forward them to the app instance
        session["execution_manager"].communication_manager.to_app_instance.send(
            {"type": "get-widget-states", "client_id": client_id}
        )
        return

    # For messages that require widget_id
    if "widget_id" not in message:
        logger.error(f"Received message without widget_id: {message}")
        return

    # Continue with the existing logic for messages that have widget_id
    session["execution_manager"].communication_manager.to_app_instance.send(
        {
            "type": message_type,  # Use the already extracted type
            "widget_id": message["widget_id"],
            "property": message.get("property"),
            "value": message.get("value"),
            "client_id": client_id,
            "action_name": message.get("action_name"),
            "args": message.get("args", []),
            "kwargs": message.get("kwargs", {}),
        }
    )


async def handle_send_message(client_id: str, session: SessionData) -> None:
    try:
        if not session[
            "execution_manager"
        ].communication_manager.from_app_instance.empty():
            # Get the message once and distribute to all clients in the session
            response = session[
                "execution_manager"
            ].communication_manager.from_app_instance.receive()
            logger.debug(f"Received message from app instance: {response}")

            # Find all connected clients for this session
            session_id = next(
                sid
                for sid, sdata in _app.state.config.sessions.items()
                if sdata == session
            )
            session_connections = _app.state.config.connections.get(session_id, {})

            # Use Union type for message
            message: (
                WidgetUpdateMessage
                | InitConfigMessage
                | ErrorMessage
                | ActionResponseMessage
            )
            if response.get("type") == MessageType.WIDGET_UPDATE.value:
                message = WidgetUpdateMessage(**response)
            elif response.get("type") == "init-config":
                message = InitConfigMessage(**response)
            elif response.get("type") == "error":
                message = ErrorMessage(**response)
            elif response.get("type") == MessageType.ACTION_RESPONSE.value:
                message = ActionResponseMessage(**response)
            else:
                logger.warning(f"Unknown message type: {response.get('type')}")
                return

            encoded_message = encode_model(message)

            # Send to all connected clients for this session
            for client_ws in session_connections.values():
                try:
                    await client_ws.send_text(encoded_message)
                except WebSocketDisconnect:
                    logger.debug(
                        "Failed to send to a client - they may be disconnected"
                    )
                    continue

        await asyncio.sleep(0.01)
    except WebSocketDisconnect:
        logger.debug(f"WebSocket disconnected for client {client_id}")
        raise


def cleanup_connection(session_id: str, client_id: str) -> None:
    if (
        session_id in _app.state.config.connections
        and client_id in _app.state.config.connections[session_id]
    ):
        logger.info(f"Client {client_id} disconnected")
        del _app.state.config.connections[session_id][client_id]


@_app.get("/numerous.js")  # type: ignore[misc]
async def serve_main_js() -> Response:
    return Response(
        content=_app.state.config.main_js, media_type="application/javascript"
    )


def create_app(  # noqa: PLR0912, C901
    template: str,
    dev: bool = False,
    widgets: dict[str, AnyWidget] | None = None,
    app_generator: Callable[[], dict[str, AnyWidget]] | None = None,
    **kwargs: dict[str, Any],
) -> NumerousApp:
    if widgets is None:
        widgets = {}

    for key, value in kwargs.items():
        if isinstance(value, AnyWidget):
            widgets[key] = value

    # Try to detect widgets in the locals from where the app function is called
    collect_widgets = len(widgets) == 0

    module_path = None

    is_process = False

    # Get the parent frame
    if (frame := inspect.currentframe()) is not None:
        frame = frame.f_back
        if frame:
            for key, value in frame.f_locals.items():
                if collect_widgets and isinstance(value, AnyWidget):
                    widgets[key] = value

            module_path = frame.f_code.co_filename

            if frame.f_locals.get("__process__"):
                is_process = True

    if module_path is None:
        raise ValueError("Could not determine app name or module path")

    allow_threaded = False
    if app_generator is not None:
        allow_threaded = True
        widgets = app_generator()

    logger.info(
        f"App instances will be {'threaded' if allow_threaded else 'multiprocessed'}"
    )
    if not is_process:
        # Optional: Configure static files (CSS, JS, images) only if directory exists
        static_dir = BASE_DIR / "static"
        if static_dir.exists():
            _app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

        # Add new mount for package static files
        package_static = PACKAGE_DIR / "static"
        if package_static.exists():
            _app.mount(
                "/numerous-static",
                StaticFiles(directory=str(package_static)),
                name="numerous_static",
            )

        config = NumerousAppServerState(
            dev=dev,
            main_js=_load_main_js(),
            sessions={},
            connections={},
            base_dir=str(BASE_DIR),
            module_path=str(module_path),
            template=template,
            internal_templates=templates,
            allow_threaded=allow_threaded,
        )

        _app.state.config = config

    if widgets:
        # Sort so ParentVisibility widgets are first in the dict
        widgets = {  # noqa: C416
            key: value
            for key, value in sorted(
                widgets.items(),
                key=lambda x: isinstance(x[1], ParentVisibility),
                reverse=True,
            )
        }

    _app.widgets = widgets

    return _app


@_app.get("/api/describe")  # type: ignore[misc]
async def describe_app() -> AppDescription:
    """
    Return a complete description of the app.

    Includes widgets, template context, and structure.
    """
    # Get template information
    template_name = _get_template(
        _app.state.config.template, _app.state.config.internal_templates
    )
    template_source = ""
    try:
        if isinstance(templates.env.loader, FileSystemLoader):
            template_source = templates.env.loader.get_source(
                templates.env, template_name
            )[0]
    except jinja2.exceptions.TemplateNotFound:
        template_source = "Template not found"

    # Parse template for context variables
    parsed_content = templates.env.parse(template_source)
    template_variables = meta.find_undeclared_variables(parsed_content)
    template_variables.discard("request")
    template_variables.discard("title")

    return AppDescription(
        app_info=AppInfo(
            dev_mode=_app.state.config.dev,
            base_dir=_app.state.config.base_dir,
            module_path=_app.state.config.module_path,
            allow_threaded=_app.state.config.allow_threaded,
        ),
        template=TemplateDescription(
            name=template_name,
            source=template_source,
            variables=list(template_variables),
        ),
        widgets=_describe_widgets(_app.widgets),
    )


@_app.get("/api/widgets/{widget_id}/traits/{trait_name}")  # type: ignore[misc]
async def get_trait_value(
    widget_id: str, trait_name: str, session_id: str
) -> TraitValue:
    """Get the current value of a widget's trait."""
    if widget_id not in _app.widgets:
        raise HTTPException(status_code=404, detail=f"Widget '{widget_id}' not found")

    widget = _app.widgets[widget_id]
    if trait_name not in widget.traits():
        raise HTTPException(
            status_code=404,
            detail=f"Trait '{trait_name}' not found on widget '{widget_id}'",
        )

    try:
        value = getattr(widget, trait_name)
        return TraitValue(
            widget_id=widget_id, trait=trait_name, value=value, session_id=session_id
        )
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error getting trait value: {e!s}"
        ) from e


@_app.put("/api/widgets/{widget_id}/traits/{trait_name}")  # type: ignore[misc]
async def set_trait_value(
    widget_id: str,
    trait_name: str,
    trait_value: SetTraitValue,
    session_id: str,
) -> TraitValue:
    """Set the value of a widget's trait."""
    session = _get_session(
        _app.state.config.allow_threaded,
        session_id,
        _app.state.config.base_dir,
        _app.state.config.module_path,
        _app.state.config.template,
        _app.state.config.sessions,
    )

    if widget_id not in _app.widgets:
        raise HTTPException(status_code=404, detail=f"Widget '{widget_id}' not found")

    widget = _app.widgets[widget_id]
    if trait_name not in widget.traits():
        raise HTTPException(
            status_code=404,
            detail=f"Trait '{trait_name}' not found on widget '{widget_id}'",
        )

    # Create widget update message using Pydantic model
    update_message = WidgetUpdateRequestMessage(
        type=MessageType.WIDGET_UPDATE,
        widget_id=widget_id,
        property=trait_name,
        value=trait_value.value,
    )

    # Send the message using the communication manager
    session["execution_manager"].communication_manager.to_app_instance.send(
        update_message.model_dump()
    )

    # Return the updated trait value
    return TraitValue(
        widget_id=widget_id,
        trait=trait_name,
        value=trait_value.value,
        session_id=session_id,
    )


async def _handle_action_response(
    response_queue: asyncio.Queue,  # type: ignore[type-arg]
    request_id: str,  # noqa: ARG001
) -> Any:  # noqa: ANN401
    """Handle the response from an action execution."""
    try:
        response = await asyncio.wait_for(response_queue.get(), timeout=10)
        action_response = ActionResponseMessage(**response)
        if action_response.error:
            raise HTTPException(status_code=500, detail=action_response.error)
        return action_response.result  # noqa: TRY300
    except TimeoutError as err:
        raise HTTPException(
            status_code=504,
            detail="Timeout waiting for action response",
        ) from err


class MockWebSocket:
    """Mock WebSocket for handling action responses."""

    def __init__(self, response_queue: asyncio.Queue, request_id: str) -> None:  # type: ignore[type-arg]
        self.response_queue = response_queue
        self.request_id = request_id

    async def send_text(self, message: str) -> None:
        """Send a message to the mock WebSocket."""
        try:
            data = json.loads(message)
            if (
                data.get("type") == MessageType.ACTION_RESPONSE.value
                and data.get("request_id") == self.request_id
            ):
                await self.response_queue.put(data)
        except json.JSONDecodeError:
            pass


@_app.post("/api/widgets/{widget_id}/actions/{action_name}")  # type: ignore[misc]
async def execute_widget_action(
    widget_id: str,
    action_name: str,
    session_id: str,
    args: list[Any] | None = None,
    kwargs: dict[str, Any] | None = None,
) -> Any:  # noqa: ANN401
    """Execute an action on a widget."""
    session = _get_session(
        _app.state.config.allow_threaded,
        session_id,
        _app.state.config.base_dir,
        _app.state.config.module_path,
        _app.state.config.template,
        _app.state.config.sessions,
    )

    if widget_id not in _app.widgets:
        raise HTTPException(status_code=404, detail=f"Widget '{widget_id}' not found")

    # Create a unique request ID and client ID
    request_id = str(uuid.uuid4())
    client_id = f"action_client_{request_id}"

    # Create response queue for this specific request
    response_queue: asyncio.Queue[dict[str, Any]] = asyncio.Queue()

    # Register this client in the connections
    if session_id not in _app.state.config.connections:
        _app.state.config.connections[session_id] = {}

    # Create a WebSocket connection for this request
    _app.state.config.connections[session_id][client_id] = MockWebSocket(
        response_queue, request_id
    )

    try:
        # Create and send the action request message
        action_request = ActionRequestMessage(
            type=MessageType.ACTION_REQUEST.value,
            widget_id=widget_id,
            action_name=action_name,
            args=tuple(args) if args is not None else None,
            kwargs=kwargs or {},
            request_id=request_id,
            client_id=client_id,
        )

        # Send the message using the communication manager
        session["execution_manager"].communication_manager.to_app_instance.send(
            action_request.model_dump()
        )

        # Wait for response with timeout
        try:
            response = await asyncio.wait_for(response_queue.get(), timeout=10)
            action_response = ActionResponseMessage(**response)
            if action_response.error:
                raise HTTPException(status_code=500, detail=action_response.error)
            return action_response.result  # noqa: TRY300
        except TimeoutError as e:
            raise HTTPException(
                status_code=504, detail="Timeout waiting for action response"
            ) from e

    finally:
        # Clean up the temporary connection
        if session_id in _app.state.config.connections:
            _app.state.config.connections[session_id].pop(client_id, None)


def _get_widget_actions(widget: AnyWidget) -> dict[str, dict[str, Any]]:
    """Get all actions defined on a widget."""
    actions = {}
    for name, member in getmembers(widget.__class__):
        if hasattr(member, "_is_action"):  # Check for action decorator
            actions[name] = {
                "name": name,
                "doc": member.__doc__ or "",
            }
    return actions
