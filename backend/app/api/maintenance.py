from fastapi import APIRouter, Query
from app.services.log_cleanup_service import log_cleanup_service

router = APIRouter()

@router.post("/maintenance/purge-logs")
def purge_old_logs(keep_last: int = Query(50, ge=1, le=500)):
    purged_count = log_cleanup_service.purge_old_history(keep_last_n=keep_last)
    return {"message": "Cleanup executed", "purged_count": purged_count}