from app.services.history_service import history_service
from app.services.agent_registry import agent_registry

class ReadinessAggregator:
    def check_readiness((self) -> dict:
        checks = {}
        try:
            history_service.get_all_logs()
            checks["database_access"] = "ok"
        except Exception as e:
            checks["database_access"] = f"error: {e}"

        checks["agent_registry"] = "ok" if len(agent_registry._registry) > 0 else "empty"
        
        is_ready = all(v == "ok" for v in checks.values())
        return {"status": "ready" if is_ready else "unready", "details": checks}

readiness_aggregator = ReadinessAggregator()