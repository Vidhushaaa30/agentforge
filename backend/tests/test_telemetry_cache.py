import time
from app.core.ttl_cache import TTLCache
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_ttl_cache_expiration():
    cache = TTLCache(default_ttl=1)
    cache.set("key1", "value1")
    assert cache.get("key1") == "value1"
    time.sleep(1.1)
    assert cache.get("key1") is None

def test_system_telemetry_endpoint():
    response = client.get("/api/telemetry/system")
    assert response.status_code == 200
    assert "cpu_usage_percent" in response.json()