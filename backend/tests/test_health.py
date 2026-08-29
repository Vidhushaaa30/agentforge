from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_system_config():
    response = client.get("/api/config")
    assert response.status_code == 200
    assert "active_model" in response.json()