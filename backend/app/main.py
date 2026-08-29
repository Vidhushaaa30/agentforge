from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.core.exceptions import AgentForgeException
from app.core.middleware import RequestLoggingMiddleware
from app.api import execution, health, prompts, config_info, storage_info, export, system, cache_info

tags_metadata = [
    {"name": "Execution", "description": "Workflow execution and history operations"},
    {"name": "System & Health", "description": "Health checks, diagnostics, and storage statistics"},
    {"name": "Configuration", "description": "System prompts and static configuration info"},
]

app = FastAPI(
    title="AgentForge API",
    description="Multi-agent workflow orchestration engine",
    version="0.2.0",
    openapi_tags=tags_metadata
)

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

@app.get("/")
def read_root():
    return {"message": "AgentForge API is running"}