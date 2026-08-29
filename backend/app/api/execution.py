from fastapi import APIRouter, HTTPException, Query, BackgroundTasks
from typing import Optional, List
import uuid
from app.schemas.requests import WorkflowExecutionRequest
from app.schemas.background import BackgroundTaskResponse
from app.schemas.batch import BatchExecutionRequest
from app.services.orchestrator import Orchestrator
from app.services.history_service import history_service
from app.services.status_service import status_service

router = APIRouter()
orchestrator = Orchestrator()

@router.post("/execute/batch")
def execute_batch_workflows(request: BatchExecutionRequest):
    batch_results = []
    for prompt in request.prompts:
        try:
            res = orchestrator.run_workflow(prompt, max_tasks=request.max_tasks_per_prompt)
            batch_results.append({"prompt": prompt, "status": "success", "data": res})
        except Exception as e:
            batch_results.append({"prompt": prompt, "status": "failed", "error": str(e)})
    return {"batch_size": len(request.prompts), "results": batch_results}