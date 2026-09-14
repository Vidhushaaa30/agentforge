import contextvars
from contextlib import contextmanager

_task_timeout_var = contextvars.ContextVar("task_timeout", default=30.0)

def get_current_timeout() -> float:
    return _task_timeout_var.get()

@contextmanager
def override_task_timeout(seconds: float):
    token = _task_timeout_var.set(seconds)
    try:
        yield
    finally:
        _task_timeout_var.reset(token)