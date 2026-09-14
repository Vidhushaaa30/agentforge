from pydantic import BaseModel, Field
from typing import List

class AgentCapability(BaseModel):
    agent_name: str
    description: str
    supported_tasks: List[str] = Field(default_factory=list)
    max_concurrent_tasks: int = Field(default=5, ge=1)