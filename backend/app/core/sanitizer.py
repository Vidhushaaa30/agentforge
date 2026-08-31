import re

def sanitize_prompt(prompt: str) -> str:
    # Strip dangerous HTML/script tags from user input
    cleaned = re.sub(r'<[^>]*>', '', prompt)
    return cleaned.strip()