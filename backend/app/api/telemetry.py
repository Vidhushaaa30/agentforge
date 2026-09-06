from fastapi import APIRouter
from app.services.system_metrics import system_metrics_service

router = APIRouter()

@router.get("/telemetry/system")
def get_system_telemetry():
    return system_metrics_service.get_system_telemetry()