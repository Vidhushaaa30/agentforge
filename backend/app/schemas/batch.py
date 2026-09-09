from pydantic import BaseModel, Field
from typing import List
from app.schemas.requests import WorkflowExecutionRequest

class BatchWorkflowExecutionRequest(BaseModel):
    requests: List[WorkflowExecutionRequest] = Field(..., min_items=1, max_items=10)
    stop_on_failure: bool = Field(default=False)