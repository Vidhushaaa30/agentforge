import asyncio
from typing import Callable, Any
from app.core.logger import logger

class AsyncTaskQueue:
    def __init__(self):
        self._queue = asyncio.Queue()
        self._is_running = False

    async def enqueue(self, task_func: Callable, *args, **kwargs):
        await self._queue.put((task_func, args, kwargs))
        logger.info("Task enqueued into async background execution queue.")

    async def start_worker(self):
        self._is_running = True
        while self._is_running:
            task_func, args, kwargs = await self._queue.get()
            try:
                if asyncio.iscoroutinefunction(task_func):
                    await task_func(*args, **kwargs)
                else:
                    task_func(*args, **kwargs)
            except Exception as e:
                logger.error(f"Error executing enqueued task: {e}")
            finally:
                self._queue.task_done()

task_queue = AsyncTaskQueue()