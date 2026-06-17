import json
from typing import Any, Optional
from backend.utils.config import config

try:
    import redis
    REDIS_AVAILABLE = True
except ImportError:
    REDIS_AVAILABLE = False


class RedisCache:
    def __init__(self, url: Optional[str] = None):
        self._client = None
        if REDIS_AVAILABLE:
            try:
                self._client = redis.from_url(url or config.REDIS_URL, decode_responses=True)
            except Exception:
                self._client = None

    def get(self, key: str) -> Optional[Any]:
        if not self._client:
            return None
        value = self._client.get(key)
        if value is None:
            return None
        try:
            return json.loads(value)
        except (json.JSONDecodeError, TypeError):
            return value

    def set(self, key: str, value: Any, ttl: Optional[int] = None):
        if not self._client:
            return
        serialized = json.dumps(value, default=str)
        if ttl:
            self._client.setex(key, ttl, serialized)
        else:
            self._client.set(key, serialized)

    def delete(self, key: str):
        if self._client:
            self._client.delete(key)

    def clear(self):
        if self._client:
            self._client.flushdb()

    def has(self, key: str) -> bool:
        if not self._client:
            return False
        return bool(self._client.exists(key))
