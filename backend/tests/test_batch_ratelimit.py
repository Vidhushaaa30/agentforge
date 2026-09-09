from app.services.rate_limiter import TokenBucketRateLimiter
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_token_bucket_consumption():
    limiter = TokenBucketRateLimiter(capacity=2, refill_rate=0.1)
    assert limiter.consume(1) is True
    assert limiter.consume(1) is True
    assert limiter.consume(1) is False

def test_batch_execution_endpoint():
    payload = {
        "requests": [
            {"prompt": "Summary task 1", "max_tasks": 1},
            {"prompt": "Summary task 2", "max_tasks": 1}
        ],
        "stop_on_failure": True
    }
    response = client.post("/api/execute/batch", json=payload)
    assert response.status_code == 200
    assert response.json()["total_requested"] == 2