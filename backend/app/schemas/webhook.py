from pydantic import BaseModel, HttpUrl, Field

class WebhookSubscription(BaseModel):
    target_url: HttpUrl
    event_type: str = Field(default="workflow.completed")
    secret_token: str = Field(..., min_length=8)