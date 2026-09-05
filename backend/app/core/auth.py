import os
from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyHeader
from app.core.key_manager import key_manager

API_KEY_HEADER = APIKeyHeader(name="X-API-Key", auto_error=False)

def verify_api_key(api_key: str = Security(API_KEY_HEADER)):
    if os.getenv("ENABLE_AUTH", "false").lower() == "true":
        if not api_key or not key_manager.is_valid(api_key):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or revoked API Key"
            )
    return api_key