from app.core.timeout_override import override_task_timeout, get_current_timeout
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_timeout_override_context():
    assert get_current_timeout() == 30.0
    with override_task_timeout(15.5):
        assert get_current_timeout() == 15.5
    assert get_current_timeout() == 30.0

def test_capabilities_endpoint():
    response = client.get("/api/agents/capabilities")
    assert response.status_code == 200
    data = response.json()
    assert data["total_count"] == 2
    assert data["capabilities"][0]["agent_name"] == "researcher"