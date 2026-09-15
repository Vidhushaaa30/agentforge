from app.schemas.webhook import WebhookSubscription
from app.services.webhook_service import webhook_service
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_webhook_subscription():
    sub = WebhookSubscription(
        target_url="http://localhost:8000/webhook-test",
        event_type="workflow.completed",
        secret_token="secret123"
    )
    webhook_service.register(sub)
    assert len(webhook_service._subscriptions) > 0

def test_deep_health_endpoint():
    response = client.get("/api/health/deep")
    assert response.status_code == 200
    assert response.json()["overall_healthy"] is True