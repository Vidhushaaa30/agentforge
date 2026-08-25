class AgentForgeException(Exception):
    """Base exception for AgentForge application."""
    pass

class WorkflowExecutionError(AgentForgeException):
    """Raised when workflow execution fails."""
    pass

class TaskValidationError(AgentForgeException):
    """Raised when task parameters fail validation."""
    pass