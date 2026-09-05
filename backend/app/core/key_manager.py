from typing import Set

class KeyManager:
    def __init__(self):
        self._valid_keys: Set[str] = {"default-dev-key"}

    def add_key(self, key: str):
        self._valid_keys.add(key)

    def revoke_key(self, key: str):
        self._valid_keys.discard(key)

    def is_valid(self, key: str) -> bool:
        return key in self._valid_keys

key_manager = KeyManager()