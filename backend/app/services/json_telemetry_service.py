from typing import Dict, Any
from app.services.analytics_service import analytics_service
from app.services.system_metrics import system_metrics_service

class JSONTelemetryService:
    @staticmethod
    def get_full_telemetry() -> Dict[str, Any]:
        stats = analytics_service.get_stats()
        system_info = system_metrics_service.get_system_telemetry()
        return {
            "analytics": stats,
            "system": system_info
        }

json_telemetry_service = JSONTelemetryService()