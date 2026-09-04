from fastapi import APIRouter
from app.services.agent_registry import agent_registry

router = APIRouter()

@router.get("/agents")
def get_registered_agents():
    return {
        "available_agents": list(agent_registry._registry.keys()),
        "total_count": len(agent_registry._registry)
    }