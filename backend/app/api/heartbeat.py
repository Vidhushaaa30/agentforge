from fastapi import APIRouter, Body
from app.services.heartbeat_service import heartbeat_service

router = APIRouter()

@router.post("/heartbeat")
def send_heartbeat(client_id: str = Body(..., embed=True)):
    heartbeat_service.record_heartbeat(client_id)
    return {"status": "ack", "active_clients": heartbeat_service.get_active_clients()}