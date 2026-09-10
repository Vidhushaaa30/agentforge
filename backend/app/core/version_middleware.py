from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from app.core.version import APP_VERSION

class APIVersionHeaderMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        response.headers["X-API-Version"] = APP_VERSION
        return response