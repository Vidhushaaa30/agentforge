import time
import psutil
from typing import Dict, Any

class SystemMetricsService:
    def __init__(self):
        self._start_time = time.time()

    def get_system_telemetry(self) -> Dict[str, Any]:
        uptime_seconds = round(time.time() - self._start_time, 2)
        cpu_usage = psutil.cpu_percent(interval=None)
        memory = psutil.virtual_memory()

        return {
            "uptime_seconds": uptime_seconds,
            "cpu_usage_percent": cpu_usage,
            "memory_used_mb": round(memory.used / (1024 * 1024), 2),
            "memory_available_mb": round(memory.available / (1024 * 1024), 2),
        }

system_metrics_service = SystemMetricsService()