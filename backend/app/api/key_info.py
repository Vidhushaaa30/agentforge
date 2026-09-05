from fastapi import APIRouter, Body
from app.core.key_manager import key_manager

router = APIRouter()

@router.post("/keys/register")
def register_key(key: str = Body(..., embed=True)):
    key_manager.add_key(key)
    return {"message": "API Key registered successfully"}

@router.post("/keys/revoke")
def revoke_key(key: str = Body(..., embed=True)):
    key_manager.revoke_key(key)
    return {"message": "API Key revoked successfully"}