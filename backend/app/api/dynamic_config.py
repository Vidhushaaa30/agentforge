from fastapi import APIRouter, Body
from typing import Dict, Any
from app.services.config_service import dynamic_config_service

router = APIRouter()

@router.get("/config/dynamic")
def get_dynamic_config():
    return dynamic_config_service.get_config()

@router.patch("/config/dynamic")
def update_dynamic_config(updates: Dict[str, Any] = Body(...)):
    dynamic_config_service.update_config(updates)
    return {"message": "Configuration updated", "current_config": dynamic_config_service.get_config()}