from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class BackgroundTaskResponse(BaseModel):
    task_id: str
    status: str = "processing"
    created_at: datetime = datetime.utcnow()
    message: str = "Workflow execution started in background"