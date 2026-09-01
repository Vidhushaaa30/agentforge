import psutil
from fastapi import APIRouter
from app.services.history_service import history_service
from app.core.version import APP_VERSION

router = APIRouter()

@router.get("/health")
def health_check():
    memory = psutil.virtual_memory()
    return {
        "status": "healthy",
        "service": "AgentForge API",
        "version": APP_VERSION,
        "memory_used_percent": memory.percent,
        "total_executions": len(history_service.get_all_logs())
    }