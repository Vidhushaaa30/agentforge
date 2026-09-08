from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional, Any

class ExecutionState(str, Enum):
    QUEUED = "queued"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

class ExecutionStatusResponse(BaseModel):
    execution_id: str
    status: ExecutionState
    progress_percent: float = Field(default=0.0, ge=0.0, le=100.0)
    result: Optional[Any] = None
    error: Optional[str] = None