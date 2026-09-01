import math
from typing import List, Dict, Any, Optional
from app.schemas.history import ExecutionLog
from app.schemas.pagination import PaginatedResponse
from app.services.storage_service import storage_service
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
        storage_service.save_json(log_id, log.model_dump())
        return log

    def get_all_logs(self) -> List[ExecutionLog]:
        return list(self._logs.values())

    def get_paginated_logs(self, page: int = 1, page_size: int = 10) -> PaginatedResponse[ExecutionLog]:
        all_logs = list(self._logs.values())
        total = len(all_logs)
        start = (page - 1) * page_size
        end = start + page_size
        items = all_logs[start:end]
        total_pages = math.ceil(total / page_size) if total > 0 else 1

        return PaginatedResponse(
            items=items,
            total=total,
            page=page,
            page_size=page_size,
            total_pages=total_pages
        )

    def get_log_by_id(self, log_id: str) -> Optional[ExecutionLog]:
        if log_id in self._logs:
            return self._logs[log_id]
        saved_data = storage_service.load_json(log_id)
        if saved_data:
            return ExecutionLog(**saved_data)
        return None

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