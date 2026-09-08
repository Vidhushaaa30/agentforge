from app.services.history_service import history_service
from app.core.logger import logger

class LogCleanupService:
    @staticmethod
    def purge_old_history(keep_last_n: int = 50) -> int:
        logs = history_service.get_all_logs()
        if len(logs) <= keep_last_n:
            return 0
        
        logs_to_remove = len(logs) - keep_last_n
        logger.info(f"Purging {logs_to_remove} old history records...")
        return logs_to_remove

log_cleanup_service = LogCleanupService()