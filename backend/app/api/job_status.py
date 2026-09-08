from fastapi import APIRouter, HTTPException
from app.services.state_store import state_store_service

router = APIRouter()

@router.get("/execution/{execution_id}/status")
def get_execution_status(execution_id: str):
    state = state_store_service.get_state(execution_id)
    if not state:
        raise HTTPException(status_code=404, detail="Execution ID not found in state store")
    return state