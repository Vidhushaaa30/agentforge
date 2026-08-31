from fastapi import APIRouter, HTTPException
from app.schemas.requests import WorkflowExecutionRequest
from app.services.orchestrator import Orchestrator
from app.core.sanitizer import sanitize_prompt

router = APIRouter()
orchestrator = Orchestrator()

@router.post("/execute")
def execute_workflow(request: WorkflowExecutionRequest):
    sanitized_text = sanitize_prompt(request.prompt)
    try:
        result = orchestrator.run_workflow(sanitized_text, max_tasks=request.max_tasks)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM Execution Error: {str(e)}")