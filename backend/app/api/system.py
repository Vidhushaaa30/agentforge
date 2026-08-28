import platform
import sys
from fastapi import APIRouter
from app.core.version import APP_VERSION

router = APIRouter()

@router.get("/system/info")
def get_system_info():
    return {
        "app_version": APP_VERSION,
        "python_version": sys.version,
        "platform": platform.platform(),
        "processor": platform.processor()
    }