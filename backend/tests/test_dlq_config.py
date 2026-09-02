from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_dlq_endpoint():
    response = client.get("/api/dlq/tasks")
    assert response.status_code == 200
    assert "failed_count" in response.json()

def test_dynamic_config_patch():
    response = client.patch("/api/config/dynamic", json={"max_retries": 5})
    assert response.status_code == 200
    assert response.json()["current_config"]["max_retries"] == 5