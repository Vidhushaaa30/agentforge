from app.core.config import get_llm
from app.schemas.planner import Task, TaskResult

class ResearcherAgent:
    def __init__(self):
        self.llm = get_llm()

    def execute(self, task: Task) -> TaskResult:
        prompt = f"Perform thorough research and gather key information for task: {task.description}"
        response = self.llm.invoke(prompt)
        return TaskResult(
            task_id=task.id,
            agent_name="researcher",
            output=response.content
        )

class WriterAgent:
    def __init__(self):
        self.llm = get_llm()

    def execute(self, task: Task, context: str = "") -> TaskResult:
        prompt = (
            f"Use the following research context:\n{context}\n\n"
            f"Write detailed content for task: {task.description}"
        )
        response = self.llm.invoke(prompt)
        return TaskResult(
            task_id=task.id,
            agent_name="writer",
            output=response.content
        )