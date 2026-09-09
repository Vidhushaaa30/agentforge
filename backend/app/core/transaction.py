from contextlib import contextmanager
from app.core.logger import logger

@contextmanager
def safe_storage_transaction():
    logger.info("Beginning safe storage operation transaction context...")
    try:
        yield
        logger.info("Storage transaction completed successfully.")
    except Exception as e:
        logger.error(f"Storage transaction aborted due to error: {e}")
        raise e