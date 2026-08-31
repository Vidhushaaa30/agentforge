from fastapi import APIRouter
from app.services.analytics_service import analytics_service

router = APIRouter()

@router.get("/analytics/stats")
def get_analytics_stats():
    return analytics_service.get_stats()