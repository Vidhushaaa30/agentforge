from fastapi import APIRouter

router = APIRouter()

@router.get("/config")
def get_system_config():
    return {
        "active_model": "gemini-2.0-flash",
        "supported_agents": ["researcher", "writer"],
        "max_tasks_limit": 10
    }