from fastapi import APIRouter
from app.core.circuit_breaker import circuit_breaker

router = APIRouter()

@router.get("/circuit-breaker/status")
def get_circuit_status():
    return {
        "state": circuit_breaker.state,
        "failure_count": circuit_breaker.failure_count,
        "allowed": circuit_breaker.allow_execution()
    }