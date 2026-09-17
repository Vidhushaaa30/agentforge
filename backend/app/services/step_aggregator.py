from typing import List, Dict, Any

class StepAggregatorService:
    def aggregate_step_outputs(self, results: List[Dict[str, Any]]) -> Dict[str, Any]:
        total_steps = len(results)
        completed_steps = sum(1 for r in results if r.get("status") == "completed")
        total_output_chars = sum(len(r.get("output", "")) for r in results)

        return {
            "total_steps": total_steps,
            "completed_steps": completed_steps,
            "completion_rate": (completed_steps / total_steps * 100) if total_steps > 0 else 0,
            "total_output_chars": total_output_chars
        }

step_aggregator = StepAggregatorService()