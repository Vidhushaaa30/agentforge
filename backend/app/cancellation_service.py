from typing import Set

class CancellationService:
    def __init__(self):
        self._cancelled_jobs: Set[str] = set()

    def cancel_job(self, execution_id: str):
        self._cancelled_jobs.add(execution_id)

    def is_cancelled(self, execution_id: str) -> bool:
        return execution_id in self._cancelled_jobs

cancellation_service = CancellationService()