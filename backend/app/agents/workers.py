from app.schemas.tasks import TaskItem, TaskResult
from app.services.worker_load import worker_load_tracker

class ResearcherAgent:
    def execute(self, task: TaskItem) -> TaskResult:
        worker_load_tracker.increment_load("researcher")
        try:
            output = f"Research insights for '{task.title}': Gathered initial context and key factual points."
            return TaskResult(task_id=task.id, status="completed", output=output)
        finally:
            worker_load_tracker.decrement_load("researcher")

class WriterAgent:
    def execute(self, task: TaskItem, context: str = "") -> TaskResult:
        worker_load_tracker.increment_load("writer")
        try:
            output = f"Drafted section for '{task.title}'. Incorporating context length: {len(context)} chars."
            return TaskResult(task_id=task.id, status="completed", output=output)
        finally:
            worker_load_tracker.decrement_load("writer")