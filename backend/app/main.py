from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import execution, health

app = FastAPI(title="AgentForge API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(execution.router, prefix="/api")
app.include_router(health.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "AgentForge API is running"}