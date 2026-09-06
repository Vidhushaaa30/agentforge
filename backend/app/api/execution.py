from fastapi import APIRouter, HTTPException, Depends
from app.schemas.requests import WorkflowExecutionRequest
from app.services.orchestrator import Orchestrator
from app.core.sanitizer import sanitize_prompt
from app.core.guardrails import check_prompt_safety
from app.core.dependencies import get_orchestrator
from app.core.auth import verify_api_key
from app.core.ttl_cache import ttl_cache

router = APIRouter()

@router.post("/execute", dependencies=[Depends(verify_api_key)])
def execute_workflow(
    request: WorkflowExecutionRequest,
    orchestrator: Orchestrator = Depends(get_orchestrator)
):
    check_prompt_safety(request.prompt)
    sanitized_text = sanitize_prompt(request.prompt)
    
    cache_key = f"exec:{hash(sanitized_text)}:{request.max_tasks}"
    cached_response = ttl_cache.get(cache_key)
    if cached_response:
        return cached_response

    try:
        result = orchestrator.run_workflow(sanitized_text, max_tasks=request.max_tasks)
        ttl_cache.set(cache_key, result, ttl=120)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM Execution Error: {str(e)}")