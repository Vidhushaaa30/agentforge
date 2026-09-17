import urllib.request
import json
from app.schemas.callback import ExecutionCallbackRequest
from app.core.logger import logger

class CallbackService:
    def trigger_callback(self, config: ExecutionCallbackRequest, payload: dict):
        try:
            data = json.dumps(payload).encode("utf-8")
            req = urllib.request.Request(
                str(config.callback_url),
                data=data,
                headers={"Content-Type": "application/json", **(config.custom_headers or {})}
            )
            with urllib.request.urlopen(req, timeout=5) as response:
                logger.info(f"Callback dispatched to {config.callback_url}. Status: {response.status}")
        except Exception as e:
            logger.error(f"Failed to dispatch callback to {config.callback_url}: {e}")

callback_service = CallbackService()