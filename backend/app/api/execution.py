from fastapi import APIRouter, HTTPException, Query
from typing import Optional
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
def get_execution_history(q: Optional[str] = Query(None, description="Search keyword for filtering prompts")):
    if q:
        return history_service.search_logs_by_keyword(q)
    return history_service.get_all_logs()

@router.get("/history/{log_id}")
def get_execution_log(log_id: str):
    log = history_service.get_log_by_id(log_id)
    if not log:
        raise HTTPException(status_code=404, detail="Execution log not found")
    return log