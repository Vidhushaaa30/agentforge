from fastapi import APIRouter
from app.services.cache_service import cache_service

router = APIRouter()

@router.delete("/cache")
def clear_cache():
    count = len(cache_service._cache)
    cache_service._cache.clear()
    return {"message": f"Cleared {count} item(s) from execution cache"}