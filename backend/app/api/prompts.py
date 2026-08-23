from fastapi import APIRouter
from app.core.prompts import SYSTEM_PROMPTS

router = APIRouter()

@router.get("/prompts")
def get_prompts():
    return SYSTEM_PROMPTS