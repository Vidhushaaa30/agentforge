from typing import Set

class CancellationService:
    def __init__(self):
        self._cancelled_ids: Set[str] = set()

    def cancel_execution(self, execution_id: str):
        self._cancelled_ids.add(execution_id)

    def is_cancelled(self, execution_id: str) -> bool:
        return execution_id in self._cancelled_ids

    def clear(self, execution_id: str):
        self._cancelled_ids.discard(execution_id)

cancellation_service = CancellationService()