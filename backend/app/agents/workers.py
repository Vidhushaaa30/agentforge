from app.schemas.tasks import TaskItem, TaskResult
from app.schemas.capabilities import AgentCapability

class ResearcherAgent:
    @property
    def capability(self) -> AgentCapability:
        return AgentCapability(
            agent_name="researcher",
            description="Performs data gathering, web research, and factual aggregation.",
            supported_tasks=["research", "gather", "search", "analyze"],
            max_concurrent_tasks=3
        )

    def execute(self, task: TaskItem) -> TaskResult:
        output = f"Research insights for '{task.title}': Gathered initial context and key factual points."
        return TaskResult(task_id=task.id, status="completed", output=output)

class WriterAgent:
    @property
    def capability(self) -> AgentCapability:
        return AgentCapability(
            agent_name="writer",
            description="Synthesizes findings into human-readable markdown summaries.",
            supported_tasks=["write", "summarize", "format", "draft"],
            max_concurrent_tasks=5
        )

    def execute(self, task: TaskItem, context: str = "") -> TaskResult:
        output = f"Drafted section for '{task.title}'. Incorporating context length: {len(context)} chars."
        return TaskResult(task_id=task.id, status="completed", output=output)