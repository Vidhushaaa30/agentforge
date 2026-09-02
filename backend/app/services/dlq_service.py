from typing import List, Dict, Any

class DeadLetterQueueService:
    def __init__(self):
        self._failed_tasks: List[Dict[str, Any]] = []

    def log_failure(self, job_id: str, error_message: str, payload: Dict[str, Any]):
        self._failed_tasks.append({
            "job_id": job_id,
            "error": error_message,
            "payload": payload
        })

    def get_failed_tasks(self) -> List[Dict[str, Any]]:
        return self._failed_tasks

    def clear(self):
        self._failed_tasks.clear()

dlq_service = DeadLetterQueueService()