from pydantic import BaseModel, Field
from typing import Optional

class ExecutionOptions(BaseModel):
    temperature: Optional[float] = Field(default=0.7, ge=0.0, le=1.0)
    verbose: bool = Field(default=False)

class WorkflowExecutionRequest(BaseModel):
    prompt: str = Field(..., min_length=5, description="Prompt to generate and execute an agent workflow")
    max_tasks: int = Field(default=5, ge=1, le=10, description="Maximum number of tasks allowed")
    options: Optional[ExecutionOptions] = Field(default_factory=ExecutionOptions)