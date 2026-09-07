import asyncio
from typing import Dict, Any
from app.services.orchestrator import Orchestrator

class BackgroundWorker:
    async def process_async_workflow(self, prompt: str, max_tasks: int, execution_id: str) -> Dict[str, Any]:
        orchestrator = Orchestrator()
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(
            None, orchestrator.run_workflow, prompt, max_tasks, execution_id
        )
        return result

background_worker = BackgroundWorker()