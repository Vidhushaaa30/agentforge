from fastapi import APIRouter, HTTPException, Query, Depends
from app.schemas.requests import WorkflowExecutionRequest
from app.services.orchestrator import Orchestrator
from app.services.history_service import history_service
from app.core.auth import verify_api_key
from app.core.dependencies import get_orchestrator

router = APIRouter()

@router.post("/execute", dependencies=[Depends(verify_api_key)])
def execute_workflow(
    request: WorkflowExecutionRequest,
    orchestrator: Orchestrator = Depends(get_orchestrator)
):
    try:
        result = orchestrator.run_workflow(request.prompt, max_tasks=request.max_tasks)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM Execution Error: {str(e)}")