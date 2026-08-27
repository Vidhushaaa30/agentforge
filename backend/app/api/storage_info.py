import os
from fastapi import APIRouter

router = APIRouter()

@router.get("/storage/stats")
def get_storage_stats():
    storage_dir = "storage"
    if not os.path.exists(storage_dir):
        return {"total_files": 0, "storage_path": os.path.abspath(storage_dir)}
    
    files = [f for f in os.listdir(storage_dir) if f.endswith(".json")]
    return {
        "total_files": len(files),
        "storage_path": os.path.abspath(storage_dir)
    }