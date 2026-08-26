from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.core.exceptions import AgentForgeException
from app.core.middleware import RequestLoggingMiddleware
from app.api import execution, health, prompts, config_info

app = FastAPI(title="AgentForge API")

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

app.include_router(execution.router, prefix="/api")
app.include_router(health.router, prefix="/api")
app.include_router(prompts.router, prefix="/api")
app.include_router(config_info.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "AgentForge API is running"}