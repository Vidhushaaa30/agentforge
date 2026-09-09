from fastapi import APIRouter, Depends
from app.schemas.batch import BatchWorkflowExecutionRequest
from app.services.batch_service import batch_service
from app.core.auth import verify_api_key

router = APIRouter()

@router.post("/execute/batch", dependencies=[Depends(verify_api_key)])
def execute_batch_workflows(batch_req: BatchWorkflowExecutionRequest):
    results = batch_service.process_batch(batch_req.requests, stop_on_failure=batch_req.stop_on_failure)
    return {"total_requested": len(batch_req.requests), "batch_results": results}