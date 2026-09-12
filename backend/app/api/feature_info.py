from fastapi import APIRouter, Body
from app.services.feature_flags import feature_flag_service

router = APIRouter()

@router.get("/features")
def get_features():
    return {"flags": feature_flag_service.get_all_flags()}

@router.post("/features/toggle")
def toggle_feature(feature_name: str = Body(..., embed=True), enabled: bool = Body(..., embed=True)):
    feature_flag_service.set_flag(feature_name, enabled)
    return {"message": f"Feature '{feature_name}' updated to {enabled}"}