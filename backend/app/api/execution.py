from fastapi import APIRouter, HTTPException, Depends
from app.schemas.requests import WorkflowExecutionRequest
from app.services.orchestrator import Orchestrator
from app.core.sanitizer import sanitize_prompt
from app.core.guardrails import check_prompt_safety
from app.core.dependencies import get_orchestrator
from app.core.auth import verify_api_key

router = APIRouter()

@router.post("/execute", dependencies=[Depends(verify_api_key)])
def execute_workflow(
    request: WorkflowExecutionRequest,
    orchestrator: Orchestrator = Depends(get_orchestrator)
):
    check_prompt_safety(request.prompt)
    sanitized_text = sanitize_prompt(request.prompt)
    try:
        result = orchestrator.run_workflow(sanitized_text, max_tasks=request.max_tasks)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM Execution Error: {str(e)}")