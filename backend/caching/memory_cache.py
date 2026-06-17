import time
from typing import Any, Optional


class MemoryCache:
    def __init__(self):
        self._cache = {}

    def get(self, key: str) -> Optional[Any]:
        if key not in self._cache:
            return None
        value, expiry = self._cache[key]
        if expiry is not None and time.time() > expiry:
            del self._cache[key]
            return None
        return value

    def set(self, key: str, value: Any, ttl: Optional[int] = None):
        expiry = time.time() + ttl if ttl else None
        self._cache[key] = (value, expiry)

    def delete(self, key: str):
        self._cache.pop(key, None)

    def clear(self):
        self._cache.clear()

    def has(self, key: str) -> bool:
        return self.get(key) is not None

    def size(self) -> int:
        return len(self._cache)
