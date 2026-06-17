from enum import Enum
from typing import Any, Optional


class CacheStrategy(Enum):
    LRU = "lru"
    TTL = "ttl"
    FIFO = "fifo"


class LRUCache:
    def __init__(self, capacity: int = 1000):
        self.capacity = capacity
        self._cache = {}
        self._order = []

    def get(self, key: str) -> Optional[Any]:
        if key not in self._cache:
            return None
        self._order.remove(key)
        self._order.append(key)
        return self._cache[key]

    def set(self, key: str, value: Any, ttl: Optional[int] = None):
        if key in self._cache:
            self._order.remove(key)
        elif len(self._cache) >= self.capacity:
            oldest = self._order.pop(0)
            del self._cache[oldest]
        self._cache[key] = value
        self._order.append(key)

    def delete(self, key: str):
        if key in self._cache:
            self._order.remove(key)
            del self._cache[key]

    def clear(self):
        self._cache.clear()
        self._order.clear()

    def has(self, key: str) -> bool:
        return key in self._cache


class FIFOCache:
    def __init__(self, capacity: int = 1000):
        self.capacity = capacity
        self._cache = {}
        self._order = []

    def get(self, key: str) -> Optional[Any]:
        return self._cache.get(key)

    def set(self, key: str, value: Any, ttl: Optional[int] = None):
        if key not in self._cache:
            if len(self._cache) >= self.capacity:
                oldest = self._order.pop(0)
                del self._cache[oldest]
            self._order.append(key)
        self._cache[key] = value

    def delete(self, key: str):
        if key in self._cache:
            self._order.remove(key)
            del self._cache[key]

    def clear(self):
        self._cache.clear()
        self._order.clear()

    def has(self, key: str) -> bool:
        return key in self._cache
