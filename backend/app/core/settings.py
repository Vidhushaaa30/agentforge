import os
from pydantic import BaseModel

class AppSettings(BaseModel):
    app_name: str = "AgentForge API"
    environment: str = os.getenv("APP_ENV", "development")
    debug: bool = os.getenv("DEBUG", "true").lower() == "true"
    max_tasks_allowed: int = int(os.getenv("MAX_TASKS_ALLOWED", "10"))

settings = AppSettings()