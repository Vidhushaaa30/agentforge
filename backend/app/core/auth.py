import os
from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyHeader

API_KEY_HEADER = APIKeyHeader(name="X-API-Key", auto_error=False)
EXPECTED_API_KEY = os.getenv("AGENTFORGE_API_KEY", "default-dev-key")

def verify_api_key(api_key: str = Security(API_KEY_HEADER)):
    if os.getenv("ENABLE_AUTH", "false").lower() == "true":
        if api_key != EXPECTED_API_KEY:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or missing API Key"
            )
    return api_key