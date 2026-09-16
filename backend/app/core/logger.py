import logging
from app.core.correlation import get_correlation_id

class CorrelationFilter(logging.Filter):
    def filter(self, record):
        record.correlation_id = get_correlation_id() or "N/A"
        return True

logger = logging.getLogger("agentforge")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] [corr_id:%(correlation_id)s] %(message)s")
handler.setFormatter(formatter)

logger.addFilter(CorrelationFilter())
if not logger.handlers:
    logger.addHandler(handler)