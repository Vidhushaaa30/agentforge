from fastapi import APIRouter, HTTPException
from app.schemas.requests import WorkflowExecutionRequest
from app.services.orchestrator import Orchestrator
from app.services.history_service import history_service

router = APIRouter()
orchestrator = Orchestrator()

@router.post("/execute")
def execute_workflow(request: WorkflowExecutionRequest):
    try:
        result = orchestrator.run_workflow(request.prompt, max_tasks=request.max_tasks)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM Execution Error: {str(e)}")

@router.get("/history")
def get_execution_history():
    return history_service.get_all_logs()