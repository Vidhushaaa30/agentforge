from enum import Enum
from pydantic import BaseModel, Field

class TaskPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class PriorityExecutionOptions(BaseModel):
    priority: TaskPriority = Field(default=TaskPriority.MEDIUM)
    timeout_seconds: float = Field(default=30.0, ge=1.0, le=300.0)