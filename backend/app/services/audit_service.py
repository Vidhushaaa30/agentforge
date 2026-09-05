import time
from typing import List, Dict, Any

class AuditService:
    def __init__(self):
        self._events: List[Dict[str, Any]] = []

    def log_event(self, action: str, details: Dict[str, Any]):
        self._events.append({
            "action": action,
            "details": details,
            "timestamp": time.time()
        })

    def get_events(self) -> List[Dict[str, Any]]:
        return self._events

audit_service = AuditService()