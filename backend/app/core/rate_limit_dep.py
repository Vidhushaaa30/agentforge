from fastapi import HTTPException, status
from app.services.rate_limiter import rate_limiter

def check_rate_limit():
    if not rate_limiter.consume(1):
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Rate limit exceeded. Please wait before issuing more execution requests."
        )