from app.services.step_aggregator import StepAggregatorService
from app.services.capability_registry import CapabilityRegistry
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_step_aggregator_calculation():
    aggregator = StepAggregatorService()
    mock_results = [
        {"status": "completed", "output": "12345"},
        {"status": "completed", "output": "67890"}
    ]
    aggregated = aggregator.aggregate_step_outputs(mock_results)
    assert aggregated["total_steps"] == 2
    assert aggregated["completed_steps"] == 2
    assert aggregated["completion_rate"] == 100.0
    assert aggregated["total_output_chars"] == 10

def test_capability_registry():
    registry = CapabilityRegistry()
    assert "web_search" in registry.get_capabilities_for_agent("researcher")
    registry.register_capability("researcher", "data_visualization")
    assert "data_visualization" in registry.get_capabilities_for_agent("researcher")

def test_capability_endpoint():
    response = client.get("/api/agents/researcher/capabilities")
    assert response.status_code == 200
    assert response.json()["agent_name"] == "researcher"