from typing import Dict, List

class CapabilityRegistry:
    def __init__(self):
        self._capabilities: Dict[str, List[str]] = {
            "researcher": ["web_search", "data_gathering", "fact_checking"],
            "writer": ["content_drafting", "summarization", "markdown_formatting"]
        }

    def get_capabilities_for_agent(self, agent_name: str) -> List[str]:
        return self._capabilities.get(agent_name.lower(), [])

    def register_capability(self, agent_name: str, capability: str):
        agent_key = agent_name.lower()
        if agent_key not in self._capabilities:
            self._capabilities[agent_key] = []
        if capability not in self._capabilities[agent_key]:
            self._capabilities[agent_key].append(capability)

capability_registry = CapabilityRegistry()