from fastapi import APIRouter
from app.agents.workers import ResearcherAgent, WriterAgent

router = APIRouter()

@router.get("/agents/capabilities")
def get_agent_capabilities():
    agents = [ResearcherAgent(), WriterAgent()]
    capabilities = [agent.capability for agent in agents]
    return {"capabilities": capabilities, "total_count": len(capabilities)}