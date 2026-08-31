from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_analytics_endpoint():
    response = client.get("/api/analytics/stats")
    assert response.status_code == 200
    data = response.json()
    assert "total_runs" in data
    assert "success_rate" in data