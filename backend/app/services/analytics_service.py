from typing import Dict, Any

class AnalyticsService:
    def __init__(self):
        self.total_runs = 0
        self.total_failed = 0

    def record_run(self, success: bool):
        self.total_runs += 1
        if not success:
            self.total_failed += 1

    def get_stats(self) -> Dict[str, Any]:
        return {
            "total_runs": self.total_runs,
            "total_failed": self.total_failed,
            "success_rate": round(((self.total_runs - self.total_failed) / self.total_runs * 100), 2) if self.total_runs > 0 else 100.0
        }

analytics_service = AnalyticsService()