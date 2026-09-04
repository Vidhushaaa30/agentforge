from typing import Dict, Any
from app.services.analytics_service import analytics_service

class TelemetryService:
    @staticmethod
    def get_prometheus_metrics() -> str:
        stats = analytics_service.get_stats()
        lines = [
            "# HELP agentforge_total_runs Total number of workflow executions",
            "# TYPE agentforge_total_runs counter",
            f"agentforge_total_runs {stats.get('total_runs', 0)}",
            "# HELP agentforge_total_failed Total number of failed executions",
            "# TYPE agentforge_total_failed counter",
            f"agentforge_total_failed {stats.get('total_failed', 0)}",
            "# HELP agentforge_success_rate Workflow execution success percentage",
            "# TYPE agentforge_success_rate gauge",
            f"agentforge_success_rate {stats.get('success_rate', 100.0)}"
        ]
        return "\n".join(lines) + "\n"

telemetry_service = TelemetryService()