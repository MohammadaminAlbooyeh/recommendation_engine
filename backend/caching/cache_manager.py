from typing import Any, Optional
from backend.caching.memory_cache import MemoryCache
from backend.caching.redis_cache import RedisCache
from backend.caching.cache_strategies import LRUCache, FIFOCache, CacheStrategy
from backend.utils.config import config


class CacheManager:
    def __init__(self, strategy: str = "ttl"):
        self.strategy = strategy
        self._local = MemoryCache()
        self._redis = RedisCache()
        self._lru = LRUCache()
        self._fifo = FIFOCache()

    def get(self, key: str) -> Optional[Any]:
        if self.strategy == "redis":
            return self._redis.get(key)
        elif self.strategy == "lru":
            return self._lru.get(key)
        elif self.strategy == "fifo":
            return self._fifo.get(key)
        return self._local.get(key)

    def set(self, key: str, value: Any, ttl: Optional[int] = None):
        ttl = ttl or config.CACHE_TTL
        self._local.set(key, value, ttl)
        if self.strategy == "redis":
            self._redis.set(key, value, ttl)
        elif self.strategy == "lru":
            self._lru.set(key, value, ttl)
        elif self.strategy == "fifo":
            self._fifo.set(key, value, ttl)

    def delete(self, key: str):
        self._local.delete(key)
        self._redis.delete(key)
        self._lru.delete(key)
        self._fifo.delete(key)

    def clear(self):
        self._local.clear()
        self._redis.clear()
        self._lru.clear()
        self._fifo.clear()

    def has(self, key: str) -> bool:
        return self._local.has(key) or self._redis.has(key)
