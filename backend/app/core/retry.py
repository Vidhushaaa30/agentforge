import time
import functools
from app.core.logger import logger

def retry_on_exception(retries: int = 3, delay: float = 1.0, backoff: float = 2.0):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == retries:
                        logger.error(f"Function {func.__name__} failed after {retries} attempts.")
                        raise e
                    logger.warning(f"Attempt {attempt} for {func.__name__} failed: {e}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator