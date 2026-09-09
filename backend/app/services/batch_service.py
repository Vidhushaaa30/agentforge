from typing import List, Dict, Any
from app.schemas.requests import WorkflowExecutionRequest
from app.services.orchestrator import Orchestrator

class BatchExecutionService:
    def __init__(self):
        self.orchestrator = Orchestrator()

    def process_batch(self, requests: List[WorkflowExecutionRequest], stop_on_failure: bool = False) -> List[Dict[str, Any]]:
        results = []
        for req in requests:
            try:
                res = self.orchestrator.run_workflow(req.prompt, max_tasks=req.max_tasks)
                results.append({"status": "success", "result": res})
            except Exception as e:
                results.append({"status": "failed", "error": str(e)})
                if stop_on_failure:
                    break
        return results

batch_service = BatchExecutionService()