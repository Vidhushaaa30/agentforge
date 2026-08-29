import time
from typing import Dict, Any, Optional

class CacheService:
    def __init__(self, ttl_seconds: int = 300):
        self.ttl = ttl_seconds
        self._cache: Dict[str, Dict[str, Any]] = {}

    def get(self, key: str) -> Optional[Any]:
        if key in self._cache:
            entry = self._cache[key]
            if time.time() - entry["timestamp"] < self.ttl:
                return entry["value"]
            del self._cache[key]
        return None

    def set(self, key: str, value: Any):
        self._cache[key] = {
            "value": value,
            "timestamp": time.time()
        }

cache_service = CacheService()