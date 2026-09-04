from typing import Dict, Any, Type
from app.agents.workers import ResearcherAgent, WriterAgent

class AgentRegistry:
    def __init__(self):
        self._registry: Dict[str, Any] = {
            "researcher": ResearcherAgent,
            "writer": WriterAgent,
        }

    def get_agent_class(self, agent_name: str):
        return self._registry.get(agent_name.lower(), WriterAgent)

    def register_agent(self, name: str, agent_cls: Type):
        self._registry[name.lower()] = agent_cls

agent_registry = AgentRegistry()