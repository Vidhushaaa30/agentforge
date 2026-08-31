from fastapi import APIRouter
from app.services.rate_limiter import rate_limiter

router = APIRouter()

@router.delete("/rate-limit/reset")
def reset_rate_limit():
    rate_limiter.reset()
    return {"message": "Rate limiter counters reset successfully."}