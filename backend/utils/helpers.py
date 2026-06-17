import time
import hashlib
import json
from typing import Any, List


def generate_cache_key(*args, **kwargs) -> str:
    raw = json.dumps((args, sorted(kwargs.items())), sort_keys=True, default=str)
    return hashlib.md5(raw.encode()).hexdigest()


def chunk_list(items: List[Any], chunk_size: int):
    for i in range(0, len(items), chunk_size):
        yield items[i:i + chunk_size]


def timed(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        return result, elapsed
    return wrapper


def safe_divide(numerator: float, denominator: float, default: float = 0.0) -> float:
    if denominator == 0:
        return default
    return numerator / denominator
