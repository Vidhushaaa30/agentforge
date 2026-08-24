from typing import List
from app.schemas.planner import Task

class TaskFilterService:
    @staticmethod
    def limit_tasks(tasks: List[Task], max_tasks: int) -> List[Task]:
        return tasks[:max_tasks]

task_filter_service = TaskFilterService()