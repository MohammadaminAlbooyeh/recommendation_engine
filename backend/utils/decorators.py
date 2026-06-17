import functools
import time
from typing import Callable
from backend.utils.logger import logger


def log_execution(func: Callable):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Executing {func.__name__}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"Completed {func.__name__}")
            return result
        except Exception as e:
            logger.error(f"Failed {func.__name__}: {str(e)}")
            raise
    return wrapper


def measure_time(func: Callable):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        logger.info(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper


def cache_result(func: Callable):
    _cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(sorted(kwargs.items()))
        if key in _cache:
            return _cache[key]
        result = func(*args, **kwargs)
        _cache[key] = result
        return result
    return wrapper
