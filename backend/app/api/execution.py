from fastapi import APIRouter
from app.services.orchestrator import Orchestrator

router = APIRouter()
orchestrator = Orchestrator()

@router.post("/execute")
def execute_workflow(prompt: str):
    return orchestrator.run_workflow(prompt)