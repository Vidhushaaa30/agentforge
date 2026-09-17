from pydantic import BaseModel, HttpUrl, Field
from typing import Optional

class ExecutionCallbackRequest(BaseModel):
    callback_url: HttpUrl
    notify_on_failure: bool = Field(default=True)
    notify_on_success: bool = Field(default=True)
    custom_headers: Optional[dict] = Field(default=None)