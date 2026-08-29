from pydantic import BaseModel, Field
from typing import List

class BatchExecutionRequest(BaseModel):
    prompts: List[str] = Field(..., min_items=1, max_items=5, description="List of prompts to execute in batch")
    max_tasks_per_prompt: int = Field(default=3, ge=1, le=5)