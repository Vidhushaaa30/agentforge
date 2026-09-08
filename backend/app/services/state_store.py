from typing import Dict, Any, Optional

class StateStoreService:
    def __init__(self):
        self._states: Dict[str, Dict[str, Any]] = {}

    def set_state(self, key: str, value: Dict[str, Any]):
        self._states[key] = value

    def get_state(self, key: str) -> Optional[Dict[str, Any]]:
        return self._states.get(key)

    def delete_state(self, key: str):
        self._states.pop(key, None)

state_store_service = StateStoreService()