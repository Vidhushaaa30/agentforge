from app.schemas.planner import Task, TaskResult

class ResearcherAgent:
    def execute(self, task: Task) -> TaskResult:
        # Mock researcher output (we'll connect real LLMs later)
        output = (
            f"[RESEARCH COMPLETE] Gathered key information and data points "
            f"for task: '{task.title}' based on description: '{task.description}'."
        )
        return TaskResult(
            task_id=task.id,
            agent_name="researcher",
            output=output
        )


class WriterAgent:
    def execute(self, task: Task, context: str = "") -> TaskResult:
        # Mock writer output using research context
        output = (
            f"[DRAFT COMPLETE] Formatted structured content for: '{task.title}'. "
            f"Incorporated Context: '{context}'"
        )
        return TaskResult(
            task_id=task.id,
            agent_name="writer",
            output=output
        )