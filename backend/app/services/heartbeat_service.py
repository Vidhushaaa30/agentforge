import time
from typing import Dict

class HeartbeatService:
    def __init__(self):
        self._active_clients: Dict[str, float] = {}

    def record_heartbeat(self, client_id: str):
        self._active_clients[client_id] = time.time()

    def get_active_clients(self, ttl_seconds: float = 60.0) -> int:
        now = time.time()
        active = [cid for cid, last_seen in self._active_clients.items() if now - last_seen <= ttl_seconds]
        return len(active)

heartbeat_service = HeartbeatService()