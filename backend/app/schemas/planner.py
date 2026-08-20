from pydantic import BaseModel
from typing import List

class Task(BaseModel):
    id: int
    title: str
    description: str
    assigned_agent: str  # e.g., "researcher", "writer"

class Plan(BaseModel):
    user_prompt: str
    tasks: List[Task]