from fastapi import APIRouter
from app.schemas.webhook import WebhookSubscription
from app.services.webhook_service import webhook_service

router = APIRouter()

@router.post("/webhooks/subscribe")
def subscribe_webhook(subscription: WebhookSubscription):
    webhook_service.register(subscription)
    return {"message": "Subscription registered successfully", "event_type": subscription.event_type}