from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from app.schemas.status import ExecutionStatus
from datetime import datetime

class TaskState(BaseModel):
    task_id: int
    status: ExecutionStatus = ExecutionStatus.PENDING
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    output: Optional[str] = None
    error: Optional[str] = None