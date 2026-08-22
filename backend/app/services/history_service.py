from typing import List, Dict, Any
from app.schemas.history import ExecutionLog
import uuid
from datetime import datetime

class HistoryService:
    def __init__(self):
        self._logs: Dict[str, ExecutionLog] = {}

    def save_log(self, prompt: str, results: List[Dict[str, Any]]) -> ExecutionLog:
        log_id = str(uuid.uuid4())
        log = ExecutionLog(
            id=log_id,
            prompt=prompt,
            status="completed",
            created_at=datetime.utcnow(),
            results=results
        )
        self._logs[log_id] = log
        return log

    def get_all_logs(self) -> List[ExecutionLog]:
        return list(self._logs.values())

history_service = HistoryService()