from pydantic import BaseModel, Field

class WorkflowExecutionRequest(BaseModel):
    prompt: str = Field(..., min_length=5, description="The prompt to generate and execute an agent workflow")
    max_tasks: int = Field(default=5, ge=1, le=10, description="Maximum number of tasks allowed")