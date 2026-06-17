from fastapi import Request
from fastapi.responses import JSONResponse
from backend.utils.logger import logger
from backend.utils.exceptions import RecommendationEngineError


async def global_error_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled error on {request.method} {request.url.path}: {str(exc)}")
    if isinstance(exc, RecommendationEngineError):
        return JSONResponse(status_code=400, content={"detail": str(exc)})
    return JSONResponse(status_code=500, content={"detail": "Internal server error"})
