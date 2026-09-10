import time
from typing import Dict, Any

class ExecutionProfiler:
    def __init__(self):
        self._marks: Dict[str, float] = {}

    def start_mark(self, name: str):
        self._marks[name] = time.time()

    def end_mark(self, name: str) -> float:
        if name in self._marks:
            duration = (time.time() - self._marks[name]) * 1000
            del self._marks[name]
            return round(duration, 2)
        return 0.0

execution_profiler = ExecutionProfiler()