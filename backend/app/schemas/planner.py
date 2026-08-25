from pydantic import BaseModel
from typing import List, Optional
from app.schemas.enums import TaskStatus

class Task(BaseModel):
    id: int
    title: str
    description: str
    assigned_agent: str

class Plan(BaseModel):
    tasks: List[Task]

class TaskResult(BaseModel):
    task_id: int
    agent_name: str
    output: str
    status: TaskStatus = TaskStatus.COMPLETED
    execution_time_seconds: Optional[float] = None