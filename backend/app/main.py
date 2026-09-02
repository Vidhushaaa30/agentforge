from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from app.core.exceptions import AgentForgeException
from app.core.middleware import RequestLoggingMiddleware
from app.api import execution, health, prompts, config_info, storage_info, export, system, cache_info, analytics, rate_limit_info
from app.api import (
    execution, health, prompts, config_info, 
    storage_info, export, system, cache_info, 
    analytics, rate_limit_info, dlq_info, 
    dynamic_config, stream
)

app.include_router(dlq_info.router, prefix="/api", tags=["Execution"])
app.include_router(dynamic_config.router, prefix="/api", tags=["Configuration"])
app.include_router(stream.router, prefix="/api", tags=["Execution"])

app = FastAPI(title="AgentForge API", version="0.4.0")

app.add_middleware(GZipMiddleware, minimum_size=1000)
app.add_middleware(RequestLoggingMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(AgentForgeException)
async def custom_exception_handler(request: Request, exc: AgentForgeException):
    return JSONResponse(
        status_code=400,
        content={"error": type(exc).__name__, "detail": str(exc)}
    )

app.include_router(execution.router, prefix="/api", tags=["Execution"])
app.include_router(health.router, prefix="/api", tags=["System & Health"])
app.include_router(prompts.router, prefix="/api", tags=["Configuration"])
app.include_router(config_info.router, prefix="/api", tags=["Configuration"])
app.include_router(storage_info.router, prefix="/api", tags=["System & Health"])
app.include_router(export.router, prefix="/api", tags=["Execution"])
app.include_router(system.router, prefix="/api", tags=["System & Health"])
app.include_router(cache_info.router, prefix="/api", tags=["System & Health"])
app.include_router(analytics.router, prefix="/api", tags=["System & Health"])
app.include_router(rate_limit_info.router, prefix="/api", tags=["System & Health"])

@app.get("/")
def read_root():
    return {"message": "AgentForge API is running"}