import json
import time
from typing import Callable

from fastapi import Request, Response
from loguru import logger
from starlette.middleware.base import BaseHTTPMiddleware


class HttpHandler(BaseHTTPMiddleware):
    """
    HTTP请求处理中间件
    """

    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time

        # 如果请求被标记为不需要记录日志，则跳过日志记录
        if not getattr(request.state, 'no_logging', False):
            await self._log_request(request, process_time)

        return response

    @staticmethod
    async def _log_request(request: Request, process_time: float):
        """
        记录请求日志
        """
        try:
            body = await request.json() if request.method != "GET" else {}
        except:
            body = {}

        log_dict = {
            "method": request.method,
            "path": request.url.path,
            "client_ip": request.client.host,
            "headers": dict(request.headers),
            "json_body": body
        }

        logger.info("\n" + json.dumps(log_dict, indent=4, ensure_ascii=False))
        logger.info(f"[Request Process_time]: {process_time} second.")
        logger.info(
            f"{request.client.host}:{request.client.port} - \"{request.method} {request.url.path} HTTP/1.1\" {200}")

    @staticmethod
    def init_http_filter(app, context):
        """
        初始化HTTP过滤器
        """
        app.add_middleware(HttpHandler)
