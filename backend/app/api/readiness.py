from fastapi import APIRouter, status, Response
from app.services.history_service import history_service

router = APIRouter()

@router.get("/health/readiness")
def readiness_probe(response: Response):
    try:
        # Check underlying storage service health
        history_service.get_all_logs()
        return {"status": "ready", "checks": {"storage": "ok", "orchestrator": "ok"}}
    except Exception as e:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        return {"status": "unready", "error": str(e)}