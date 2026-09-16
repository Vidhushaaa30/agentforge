from fastapi import APIRouter
from app.services.worker_load import worker_load_tracker

router = APIRouter()

@router.get("/workers/load")
def get_worker_load():
    return {"load_distribution": worker_load_tracker.get_load_distribution()}