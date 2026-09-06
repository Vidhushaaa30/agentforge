import time
import uuid
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request

class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        correlation_id = request.headers.get("X-Correlation-ID", str(uuid.uuid4()))
        request.state.correlation_id = correlation_id
        
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        
        response.headers["X-Process-Time"] = str(round(process_time, 4))
        response.headers["X-Correlation-ID"] = correlation_id
        return response