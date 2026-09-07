import uuid
from fastapi import APIRouter, HTTPException, Depends, BackgroundTasks
from app.schemas.requests import WorkflowExecutionRequest
from app.services.orchestrator import Orchestrator
from app.services.background_worker import background_worker
from app.core.sanitizer import sanitize_prompt
from app.core.guardrails import check_prompt_safety
from app.core.dependencies import get_orchestrator
from app.core.auth import verify_api_key

router = APIRouter()

@router.post("/execute/async", dependencies=[Depends(verify_api_key)])
async def execute_workflow_async(
    request: WorkflowExecutionRequest,
    background_tasks: BackgroundTasks
):
    check_prompt_safety(request.prompt)
    sanitized_text = sanitize_prompt(request.prompt)
    execution_id = str(uuid.uuid4())

    background_tasks.add_task(
        background_worker.process_async_workflow,
        sanitized_text,
        request.max_tasks,
        execution_id
    )

    return {"execution_id": execution_id, "status": "queued", "message": "Task queued for background execution"}