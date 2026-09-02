from typing import Dict, Any

class DynamicConfigService:
    def __init__(self):
        self._config: Dict[str, Any] = {
            "max_retries": 3,
            "enable_caching": True,
            "timeout_seconds": 30.0
        }

    def update_config(self, updates: Dict[str, Any]):
        self._config.update(updates)

    def get_config(self) -> Dict[str, Any]:
        return self._config

dynamic_config_service = DynamicConfigService()