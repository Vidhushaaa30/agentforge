from fastapi import APIRouter
from app.services.audit_service import audit_service

router = APIRouter()

@router.get("/audit/logs")
def get_audit_trail():
    return {"total_events": len(audit_service.get_events()), "events": audit_service.get_events()}