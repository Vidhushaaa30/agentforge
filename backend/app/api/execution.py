from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.schemas.requests import WorkflowExecutionRequest
from app.services.orchestrator import Orchestrator
from app.services.history_service import history_service
from app.services.rate_limiter import rate_limiter
from app.services.cancellation_service import cancellation_service

router = APIRouter()
orchestrator = Orchestrator()

@router.post("/execute")
def execute_workflow(request: WorkflowExecutionRequest):
    rate_limiter.check_rate_limit()
    try:
        result = orchestrator.run_workflow(request.prompt, max_tasks=request.max_tasks)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM Execution Error: {str(e)}")

@router.post("/cancel/{execution_id}")
def cancel_workflow(execution_id: str):
    cancellation_service.cancel_job(execution_id)
    return {"message": f"Execution {execution_id} has been marked for cancellation."}

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

@router.delete("/history")
def clear_execution_history():
    count = history_service.clear_history()
    return {"message": f"Cleared {count} execution log entries."}