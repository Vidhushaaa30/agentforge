from app.core.config import get_llm
from app.core.prompts import SYSTEM_PROMPTS
from app.schemas.planner import Task, TaskResult

class ResearcherAgent:
    def __init__(self, temperature: float = 0.3):
        self.llm = get_llm()
        self.system_prompt = SYSTEM_PROMPTS["researcher"]

    def execute(self, task: Task) -> TaskResult:
        prompt = f"{self.system_prompt}\n\nTask: {task.description}"
        response = self.llm.invoke(prompt)
        output_text = response.content if isinstance(response.content, str) else str(response.content)
        
        return TaskResult(
            task_id=task.id,
            agent_name="researcher",
            output=output_text
        )

class WriterAgent:
    def __init__(self, temperature: float = 0.7):
        self.llm = get_llm()
        self.system_prompt = SYSTEM_PROMPTS["writer"]

    def execute(self, task: Task, context: str = "") -> TaskResult:
        prompt = (
            f"{self.system_prompt}\n\n"
            f"Context:\n{context}\n\n"
            f"Task: {task.description}"
        )
        response = self.llm.invoke(prompt)
        output_text = response.content if isinstance(response.content, str) else str(response.content)
        
        return TaskResult(
            task_id=task.id,
            agent_name="writer",
            output=output_text
        )