from typing import List, Dict, Any

class SummaryService:
    @staticmethod
    def generate_summary(results: List[Dict[str, Any]]) -> str:
        completed = len(results)
        agents_used = set(r.get("agent_name") for r in results if r.get("agent_name"))
        return f"Workflow successfully completed {completed} tasks using agents: {', '.join(agents_used)}."

summary_service = SummaryService()