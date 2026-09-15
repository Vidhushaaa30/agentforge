from typing import Dict, Any
from app.services.history_service import history_service
from app.services.agent_registry import agent_registry

class HealthProbeService:
    @staticmethod
    def run_full_diagnostics() -> Dict[str, Any]:
        storage_ok = True
        try:
            history_service.get_all_logs()
        except Exception:
            storage_ok = False

        registry_ok = len(agent_registry._registry) > 0

        return {
            "overall_healthy": storage_ok and registry_ok,
            "components": {
                "storage_layer": "healthy" if storage_ok else "unhealthy",
                "agent_registry": "healthy" if registry_ok else "unhealthy"
            }
        }

health_probe_service = HealthProbeService()