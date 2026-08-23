from pydantic import BaseModel
from typing import Dict, Any

class ExecutionMetrics(BaseModel):
    task_count: int
    total_execution_time_seconds: float
    agent_distribution: Dict[str, int]