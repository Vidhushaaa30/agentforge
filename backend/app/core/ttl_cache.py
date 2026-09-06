import time
from typing import Dict, Any, Optional

class TTLCache:
    def __init__(self, default_ttl: int = 300):
        self.default_ttl = default_ttl
        self._store: Dict[str, Dict[str, Any]] = {}

    def get(self, key: str) -> Optional[Any]:
        if key in self._store:
            entry = self._store[key]
            if time.time() < entry["expires_at"]:
                return entry["data"]
            del self._store[key]
        return None

    def set(self, key: str, value: Any, ttl: Optional[int] = None):
        expire_in = ttl if ttl is not None else self.default_ttl
        self._store[key] = {
            "data": value,
            "expires_at": time.time() + expire_in
        }

ttl_cache = TTLCache()