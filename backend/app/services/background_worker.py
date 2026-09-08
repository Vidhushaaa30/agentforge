import asyncio
from typing import Dict, Any
from app.services.orchestrator import Orchestrator
from app.services.state_store import state_store_service
from app.schemas.status import ExecutionState

class BackgroundWorker:
    async def process_async_workflow(self, prompt: str, max_tasks: int, execution_id: str) -> Dict[str, Any]:
        state_store_service.set_state(execution_id, {
            "execution_id": execution_id,
            "status": ExecutionState.RUNNING,
            "progress_percent": 10.0,
            "result": None,
            "error": None
        })
        
        try:
            orchestrator = Orchestrator()
            loop = asyncio.get_event_loop()
            result = await loop.run_in_executor(
                None, orchestrator.run_workflow, prompt, max_tasks, execution_id
            )
            
            state_store_service.set_state(execution_id, {
                "execution_id": execution_id,
                "status": ExecutionState.COMPLETED,
                "progress_percent": 100.0,
                "result": result,
                "error": None
            })
            return result
        except Exception as e:
            state_store_service.set_state(execution_id, {
                "execution_id": execution_id,
                "status": ExecutionState.FAILED,
                "progress_percent": 100.0,
                "result": None,
                "error": str(e)
            })
            raise e

background_worker = BackgroundWorker()