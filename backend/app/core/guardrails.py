from app.core.exceptions import TaskValidationError

SUSPECT_PATTERNS = ["ignore previous instructions", "system prompt override", "drop database"]

def check_prompt_safety(prompt: str):
    lowered = prompt.lower()
    for pattern in SUSPECT_PATTERNS:
        if pattern in lowered:
            raise TaskValidationError(f"Prompt failed security guardrail check: suspicious pattern detected.")