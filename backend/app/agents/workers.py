import time
from app.core.config import get_llm
from app.core.prompts import SYSTEM_PROMPTS
from app.core.retry import execute_with_retry
from app.schemas.planner import Task, TaskResult
from app.schemas.enums import TaskStatus

class ResearcherAgent:
    def __init__(self, temperature: float = 0.3):
        self.llm = get_llm()
        self.system_prompt = SYSTEM_PROMPTS["researcher"]

    def execute(self, task: Task) -> TaskResult:
        start_time = time.time()
        prompt = f"{self.system_prompt}\n\nTask: {task.description}"
        
        response = execute_with_retry(self.llm.invoke, max_retries=2, input=prompt)
        output_text = response.content if isinstance(response.content, str) else str(response.content)
        elapsed = round(time.time() - start_time, 2)
        
        return TaskResult(
            task_id=task.id,
            agent_name="researcher",
            output=output_text,
            status=TaskStatus.COMPLETED,
            execution_time_seconds=elapsed
        )

class WriterAgent:
    def __init__(self, temperature: float = 0.7):
        self.llm = get_llm()
        self.system_prompt = SYSTEM_PROMPTS["writer"]

    def execute(self, task: Task, context: str = "") -> TaskResult:
        start_time = time.time()
        prompt = (
            f"{self.system_prompt}\n\n"
            f"Context:\n{context}\n\n"
            f"Task: {task.description}"
        )
        response = execute_with_retry(self.llm.invoke, max_retries=2, input=prompt)
        output_text = response.content if isinstance(response.content, str) else str(response.content)
        elapsed = round(time.time() - start_time, 2)
        
        return TaskResult(
            task_id=task.id,
            agent_name="writer",
            output=output_text,
            status=TaskStatus.COMPLETED,
            execution_time_seconds=elapsed
        )