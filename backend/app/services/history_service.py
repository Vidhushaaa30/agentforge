from typing import List, Dict, Any, Optional
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

    def get_log_by_id(self, log_id: str) -> Optional[ExecutionLog]:
        return self._logs.get(log_id)

    def search_logs_by_keyword(self, keyword: str) -> List[ExecutionLog]:
        return [
            log for log in self._logs.values()
            if keyword.lower() in log.prompt.lower()
        ]

    def clear_history(self) -> int:
        count = len(self._logs)
        self._logs.clear()
        return count

history_service = HistoryService()