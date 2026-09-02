from fastapi import APIRouter
from app.services.dlq_service import dlq_service

router = APIRouter()

@router.get("/dlq/tasks")
def get_failed_queue_tasks():
    return {"failed_count": len(dlq_service.get_failed_tasks()), "items": dlq_service.get_failed_tasks()}

@router.delete("/dlq/tasks")
def clear_failed_queue_tasks():
    dlq_service.clear()
    return {"message": "Dead letter queue cleared successfully"}