from fastapi import APIRouter, HTTPException, Query, Depends
from typing import Optional
from app.schemas.requests import WorkflowExecutionRequest
from app.schemas.pagination import PaginationParams
from app.services.orchestrator import Orchestrator
from app.services.history_service import history_service
from app.core.auth import verify_api_key

router = APIRouter()
orchestrator = Orchestrator()

@router.post("/execute", dependencies=[Depends(verify_api_key)])
def execute_workflow(request: WorkflowExecutionRequest):
    try:
        result = orchestrator.run_workflow(request.prompt, max_tasks=request.max_tasks)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM Execution Error: {str(e)}")

@router.get("/history/paginated")
def get_paginated_history(page: int = Query(1, ge=1), page_size: int = Query(10, ge=1, le=50)):
    return history_service.get_paginated_logs(page=page, page_size=page_size)