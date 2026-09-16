from app.core.circuit_breaker import ExecutionCircuitBreaker
from app.services.worker_load import WorkerLoadTracker
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_circuit_breaker_tripping():
    cb = ExecutionCircuitBreaker(failure_threshold=2, recovery_time=10)
    assert cb.allow_execution() is True
    cb.record_failure()
    cb.record_failure()
    assert cb.allow_execution() is False
    assert cb.state == "OPEN"

def test_worker_load_tracking():
    tracker = WorkerLoadTracker()
    tracker.increment_load("tester")
    assert tracker.get_load_distribution()["tester"] == 1
    tracker.decrement_load("tester")
    assert tracker.get_load_distribution()["tester"] == 0

def test_correlation_id_header():
    response = client.get("/api/workers/load", headers={"X-Correlation-ID": "test-1234"})
    assert response.status_code == 200
    assert response.headers.get("X-Correlation-ID") == "test-1234"