from fastapi import FastAPI
from app.api.execution import router as execution_router

app = FastAPI(title="AgentForge API")

# Mount execution routes
app.include_router(execution_router, prefix="/api", tags=["Execution"])

@app.get("/health")
def health_check():
    return {"status": "ok"}