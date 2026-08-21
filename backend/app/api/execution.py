from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.orchestrator import Orchestrator

router = APIRouter()
orchestrator = Orchestrator()

class ExecutionRequest(BaseModel):
    prompt: str

@router.post("/execute")
def execute_workflow(request: ExecutionRequest):
    try:
        result = orchestrator.run_workflow(request.prompt)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM Execution Error: {str(e)}")