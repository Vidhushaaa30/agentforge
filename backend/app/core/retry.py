import time
from typing import Callable, Any

def execute_with_retry(func: Callable[..., Any], max_retries: int = 3, delay: float = 1.0, *args, **kwargs) -> Any:
    last_exception = None
    for attempt in range(max_retries):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            last_exception = e
            time.sleep(delay * (2 ** attempt))
    raise last_exception