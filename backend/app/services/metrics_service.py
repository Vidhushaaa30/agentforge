from typing import List, Dict, Any
from app.schemas.metrics import ExecutionMetrics

class MetricsService:
    @staticmethod
    def calculate_metrics(results: List[Dict[str, Any]], execution_time: float) -> ExecutionMetrics:
        task_count = len(results)
        distribution: Dict[str, int] = {}
        
        for item in results:
            agent = item.get("agent_name", "unknown")
            distribution[agent] = distribution.get(agent, 0) + 1

        return ExecutionMetrics(
            task_count=task_count,
            total_execution_time_seconds=round(execution_time, 2),
            agent_distribution=distribution
        )

metrics_service = MetricsService()