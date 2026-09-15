from fastapi import APIRouter, status, Response
from app.services.health_probe import health_probe_service

router = APIRouter()

@router.get("/health/deep")
def get_deep_health(response: Response):
    report = health_probe_service.run_full_diagnostics()
    if not report["overall_healthy"]:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    return report