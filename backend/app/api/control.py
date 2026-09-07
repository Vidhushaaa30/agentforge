from fastapi import APIRouter
from app.services.cancellation_service import cancellation_service

router = APIRouter()

@router.post("/execution/{execution_id}/cancel")
def cancel_execution(execution_id: str):
    cancellation_service.cancel_execution(execution_id)
    return {"message": f"Cancellation requested for execution {execution_id}", "status": "cancelling"}