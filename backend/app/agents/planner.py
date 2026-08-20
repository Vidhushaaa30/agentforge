from pydantic import BaseModel
from typing import List

class Task(BaseModel):
    id: int
    title: str
    description: str
    assigned_agent: str  # "researcher" or "writer"

class Plan(BaseModel):
    user_prompt: str
    tasks: List[Task]

class TaskResult(BaseModel):
    task_id: int
    agent_name: str
    output: str