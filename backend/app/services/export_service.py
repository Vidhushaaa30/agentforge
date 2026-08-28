import json
from typing import Dict, Any

class ExportService:
    @staticmethod
    def to_markdown(execution_data: Dict[str, Any]) -> str:
        md = f"# Execution Report ({execution_data.get('execution_id', 'N/A')})\n\n"
        md += f"**Summary:** {execution_data.get('summary', '')}\n\n"
        md += "## Task Results\n\n"
        for res in execution_data.get("results", []):
            md += f"### Task {res.get('task_id')} - Agent: {res.get('agent_name')}\n"
            md += f"{res.get('output')}\n\n"
        return md

export_service = ExportService()