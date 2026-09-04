import concurrent.futures
from typing import Callable, Any
from app.core.exceptions import WorkflowExecutionError

def execute_with_timeout(func: Callable[..., Any], timeout_seconds: float, *args, **kwargs) -> Any:
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(func, *args, **kwargs)
        try:
            return future.result(timeout=timeout_seconds)
        except concurrent.futures.TimeoutError:
            raise WorkflowExecutionError(f"Task processing exceeded time limit of {timeout_seconds}s")