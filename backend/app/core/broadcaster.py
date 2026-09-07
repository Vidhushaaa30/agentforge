from app.core.websocket_manager import ws_manager
from app.services.event_bus import event_bus

async def broadcast_event_listener(event_data: dict):
    message = f"EVENT: {event_data.get('type')} - {event_data.get('payload')}"
    await ws_manager.broadcast(message)

def setup_event_listeners():
    event_bus.subscribe("execution_event", broadcast_event_listener)