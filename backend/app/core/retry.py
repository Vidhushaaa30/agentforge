import time
import functools
from app.core.logger import logger
from app.core.retry_budget import retry_budget

def retry_on_exception(retries: int = 3, delay: float = 1.0, backoff: float = 2.0):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == retries or not retry_budget.can_retry():
                        logger.error(f"Function {func.__name__} failed or retry budget exhausted.")
                        raise e
                    logger.warning(f"Attempt {attempt} for {func.__name__} failed: {e}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator