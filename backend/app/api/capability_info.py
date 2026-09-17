from fastapi import APIRouter
from app.services.capability_registry import capability_registry

router = APIRouter()

@router.get("/agents/{agent_name}/capabilities")
def get_agent_capabilities(agent_name: str):
    caps = capability_registry.get_capabilities_for_agent(agent_name)
    return {"agent_name": agent_name, "capabilities": caps}