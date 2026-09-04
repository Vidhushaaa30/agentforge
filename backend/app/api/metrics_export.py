from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from app.services.telemetry_service import telemetry_service

router = APIRouter()

@router.get("/metrics/prometheus", response_class=PlainTextResponse)
def get_prometheus_metrics():
    return telemetry_service.get_prometheus_metrics()