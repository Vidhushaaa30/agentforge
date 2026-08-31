from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_storage_stats():
    response = client.get("/api/storage/stats")
    assert response.status_code == 200
    assert "total_files" in response.json()