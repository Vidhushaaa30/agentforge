from typing import List, Dict, Any
from app.schemas.webhook import WebhookSubscription
from app.core.logger import logger

class WebhookService:
    def __init__(self):
        self._subscriptions: List[WebhookSubscription] = []

    def register(self, subscription: WebhookSubscription):
        self._subscriptions.append(subscription)

    def notify_event(self, event_type: str, payload: Dict[str, Any]):
        matched = [sub for sub in self._subscriptions if sub.event_type == event_type]
        for sub in matched:
            logger.info(f"Dispatching event '{event_type}' to target {sub.target_url}")

webhook_service = WebhookService()