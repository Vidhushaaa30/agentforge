from typing import Dict, Any, Optional

class StatusService:
    def __init__(self):
        self._statuses: Dict[str, Dict[str, Any]] = {}

    def set_status(self, task_id: str, status: str, progress: int = 0, result: Optional[Any] = None):
        self._statuses[task_id] = {
            "status": status,
            "progress": progress,
            "result": result
        }

    def get_status(self, task_id: str) -> Optional[Dict[str, Any]]:
        return self._statuses.get(task_id)

status_service = StatusService()