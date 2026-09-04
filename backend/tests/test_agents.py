from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_agents_list():
    response = client.get("/api/agents")
    assert response.status_code == 200
    data = response.json()
    assert "researcher" in data["available_agents"]
    assert "writer" in data["available_agents"]

def test_prometheus_metrics_endpoint():
    response = client.get("/api/metrics/prometheus")
    assert response.status_code == 200
    assert "agentforge_total_runs" in response.text