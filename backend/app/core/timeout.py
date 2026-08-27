import concurrent.futures
from typing import Callable, Any
from fastapi import HTTPException

def run_with_timeout(func: Callable[..., Any], timeout_seconds: float, *args, **kwargs) -> Any:
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(func, *args, **kwargs)
        try:
            return future.result(timeout=timeout_seconds)
        except concurrent.futures.TimeoutError:
            raise HTTPException(status_code=504, detail=f"Task execution timed out after {timeout_seconds} seconds")