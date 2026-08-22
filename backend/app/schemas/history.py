from pydantic import BaseModel
from typing import List, Dict, Any
from datetime import datetime

class ExecutionLog(BaseModel):
    id: str
    prompt: str
    status: str
    created_at: datetime
    results: List[Dict[str, Any]]