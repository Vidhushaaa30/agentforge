from pydantic import BaseModel, Field
import uuid

class RequestContext(BaseModel):
    correlation_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    client_ip: str = Field(default="127.0.0.1")
    user_agent: str = Field(default="unknown")