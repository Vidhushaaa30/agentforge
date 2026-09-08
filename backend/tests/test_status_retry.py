import pytest
from app.core.retry import retry_on_exception
from app.services.state_store import state_store_service
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_retry_decorator_success():
    calls = 0
    @retry_on_exception(retries=3, delay=0.1)
    def flaky_function():
        nonlocal calls
        calls += 1
        if calls < 2:
            raise ValueError("Temporary glitch")
        return "success"
    
    assert flaky_function() == "success"
    assert calls == 2

def test_job_status_not_found():
    response = client.get("/api/execution/non-existent-id/status")
    assert response.status_code == 404