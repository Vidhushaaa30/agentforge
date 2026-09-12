from typing import Dict

class FeatureFlagService:
    def __init__(self):
        self._flags: Dict[str, bool] = {
            "enable_caching": True,
            "enable_profiling": True,
            "enable_async_execution": True,
            "enable_strict_guardrails": True
        }

    def is_enabled(self, feature_name: str) -> bool:
        return self._flags.get(feature_name.lower(), False)

    def set_flag(self, feature_name: str, enabled: bool):
        self._flags[feature_name.lower()] = enabled

    def get_all_flags(self) -> Dict[str, bool]:
        return self._flags

feature_flag_service = FeatureFlagService()