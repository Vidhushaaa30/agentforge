from app.core.exceptions import TaskValidationError

def validate_max_tasks_bound(max_tasks: int, limit: int = 10):
    if max_tasks > limit:
        raise TaskValidationError(f"Requested max_tasks ({max_tasks}) exceeds configured system upper bound of {limit}.")