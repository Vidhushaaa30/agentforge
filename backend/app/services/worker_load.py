from typing import Dict

class WorkerLoadTracker:
    def __init__(self):
        self._active_tasks: Dict[str, int] = {}

    def increment_load(self, agent_name: str):
        self._active_tasks[agent_name] = self._active_tasks.get(agent_name, 0) + 1

    def decrement_load(self, agent_name: str):
        if agent_name in self._active_tasks and self._active_tasks[agent_name] > 0:
            self._active_tasks[agent_name] -= 1

    def get_load_distribution(self) -> Dict[str, int]:
        return self._active_tasks.copy()

worker_load_tracker = WorkerLoadTracker()