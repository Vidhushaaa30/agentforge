from app.services.feature_flags import feature_flag_service
from app.core.retry_budget import RetryBudget
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_feature_flag_toggle():
    feature_flag_service.set_flag("test_flag", True)
    assert feature_flag_service.is_enabled("test_flag") is True
    feature_flag_service.set_flag("test_flag", False)
    assert feature_flag_service.is_enabled("test_flag") is False

def test_retry_budget_consumption():
    budget = RetryBudget(max_tokens=2, refill_per_second=0.0)
    assert budget.can_retry() is True
    assert budget.can_retry() is True
    assert budget.can_retry() is False

def test_heartbeat_endpoint():
    response = client.post("/api/heartbeat", json={"client_id": "test-client-1"})
    assert response.status_code == 200
    assert response.json()["status"] == "ack"