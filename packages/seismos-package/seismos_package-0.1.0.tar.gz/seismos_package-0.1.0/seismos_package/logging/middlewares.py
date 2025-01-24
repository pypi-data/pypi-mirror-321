import uuid

import structlog
from fastapi import Request
from flask import request as flask_request
from starlette.middleware.base import BaseHTTPMiddleware

logger = structlog.get_logger()


def add_request_context_flask():
    """Middleware for Flask applications."""
    request_id = flask_request.headers.get("X-Request-ID", str(uuid.uuid4()))
    structlog.contextvars.bind_contextvars(
        request_id=request_id, request_method=flask_request.method, request_path=flask_request.path
    )


async def add_request_context_fastapi(request: Request, call_next):
    """Middleware for FastAPI applications."""
    request_id = request.headers.get("x-amzn-trace-id")
    if not request_id:
        request_id = str(uuid.uuid4())

    structlog.contextvars.bind_contextvars(
        request_id=request_id, request_method=request.method, request_path=str(request.url)
    )
    response = await call_next(request)
    structlog.contextvars.clear_contextvars()
    return response


class FastAPIRequestContextMiddleware(BaseHTTPMiddleware):
    """Middleware class for FastAPI using BaseHTTPMiddleware."""

    async def dispatch(self, request: Request, call_next):
        return await add_request_context_fastapi(request, call_next)
