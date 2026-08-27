import json
import os
from typing import Dict, Any, List

class FileStorageService:
    def __init__(self, storage_dir: str = "storage"):
        self.storage_dir = storage_dir
        os.makedirs(self.storage_dir, exist_ok=True)

    def save_json(self, filename: str, data: Dict[str, Any]) -> str:
        filepath = os.path.join(self.storage_dir, f"{filename}.json")
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, default=str)
        return filepath

    def load_json(self, filename: str) -> Dict[str, Any]:
        filepath = os.path.join(self.storage_dir, f"{filename}.json")
        if not os.path.exists(filepath):
            return {}
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)

storage_service = FileStorageService()