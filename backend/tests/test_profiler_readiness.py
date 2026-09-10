from app.services.profiler import ExecutionProfiler
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_execution_profiler():
    profiler = ExecutionProfiler()
    profiler.start_mark("unit_test")
    duration = profiler.end_mark("unit_test")
    assert duration >= 0.0

def test_readiness_probe_endpoint():
    response = client.get("/api/health/readiness")
    assert response.status_code == 200
    assert response.json()["status"] == "ready"
    assert response.headers.get("x-api-version") is not None