import queue
from typing import Dict, Any, Optional

class TaskQueueService:
    def __init__(self):
        self._queue = queue.Queue()
        self._active_jobs: Dict[str, Dict[str, Any]] = {}

    def enqueue_job(self, job_id: str, payload: Dict[str, Any]):
        job_data = {"job_id": job_id, "payload": payload, "status": "queued"}
        self._active_jobs[job_id] = job_data
        self._queue.put(job_data)

    def get_next_job((self) -> Optional[Dict[str, Any]]:
        try:
            return self._queue.get_nowait()
        except queue.Empty:
            return None

    def get_job_info(self, job_id: str) -> Optional[Dict[str, Any]]:
        return self._active_jobs.get(job_id)

task_queue_service = TaskQueueService()