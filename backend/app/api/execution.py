from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.orchestrator import Orchestrator
from app.services.history_service import history_service

router = APIRouter()
orchestrator = Orchestrator()

class ExecutionRequest(BaseModel):
    prompt: str

@router.post("/execute")
def execute_workflow(request: ExecutionRequest):
    try:
        result = orchestrator.run_workflow(request.prompt)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM Execution Error: {str(e)}")

@router.get("/history")
def get_execution_history():
    return history_service.get_all_logs()