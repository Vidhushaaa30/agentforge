from pydantic import BaseModel, Field
from typing import Dict, Any

class ExecutionProfile(BaseModel):
    execution_id: str
    total_duration_ms: float
    step_durations_ms: Dict[str, float] = Field(default_factory=dict)
    memory_delta_mb: float = 0.0