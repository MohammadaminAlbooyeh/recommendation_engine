import time
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from backend.utils.logger import logger


class TimingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start = time.perf_counter()
        response = await call_next(request)
        elapsed = time.perf_counter() - start
        response.headers["X-Process-Time"] = f"{elapsed:.4f}"
        if elapsed > 1.0:
            logger.warning(f"Slow request: {request.method} {request.url.path} took {elapsed:.3f}s")
        return response
