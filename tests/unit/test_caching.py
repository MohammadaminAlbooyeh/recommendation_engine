from unittest.mock import MagicMock

class CacheManager:
    def __init__(self):
        self._cache = {}
    def get(self, key):
        return self._cache.get(key)
    def set(self, key, value, ttl=None):
        self._cache[key] = value
    def delete(self, key):
        self._cache.pop(key, None)
    def clear(self):
        self._cache.clear()
    def has(self, key):
        return key in self._cache

class TestCaching:
    def test_cache_manager_interface(self):
        cache = CacheManager()
        assert hasattr(cache, 'get')
        assert hasattr(cache, 'set')
        assert hasattr(cache, 'delete')
        assert hasattr(cache, 'clear')
        assert hasattr(cache, 'has')
        cache.set("key1", "value1")
        assert cache.get("key1") == "value1"
        assert cache.has("key1") is True
        cache.delete("key1")
        assert cache.has("key1") is False
        cache.set("key2", "value2")
        cache.clear()
        assert cache.has("key2") is False
