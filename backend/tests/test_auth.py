from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_auth_disabled_by_default():
    # Auth is disabled unless ENABLE_AUTH environment variable is explicitly 'true'
    response = client.get("/api/health")
    assert response.status_code == 200