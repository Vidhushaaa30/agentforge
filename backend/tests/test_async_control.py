from fastapi.testclient import TestClient
from app.main import app
from app.services.cancellation_service import cancellation_service

client = TestClient(app)

def test_cancel_execution_endpoint():
    response = client.post("/api/execution/test-exec-123/cancel")
    assert response.status_code == 200
    assert response.json()["status"] == "cancelling"
    assert cancellation_service.is_cancelled("test-exec-123") is True

def test_async_execute_endpoint():
    response = client.post("/api/execute/async", json={"prompt": "Write a short summary of quantum computing", "max_tasks": 2})
    assert response.status_code == 200
    assert response.json()["status"] == "queued"
    assert "execution_id" in response.json()