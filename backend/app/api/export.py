from fastapi import APIRouter, HTTPException
from fastapi.responses import PlainTextResponse
from app.services.history_service import history_service
from app.services.export_service import export_service

router = APIRouter()

@router.get("/export/{log_id}/markdown", response_class=PlainTextResponse)
def export_log_as_markdown(log_id: str):
    log = history_service.get_log_by_id(log_id)
    if not log:
        raise HTTPException(status_code=404, detail="Execution log not found")
    return export_service.to_markdown(log.model_dump())