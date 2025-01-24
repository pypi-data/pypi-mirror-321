import time
from typing import Callable

from fastapi import Request
from loguru import logger
from starlette.responses import Response


class HttpHandler:
    """
    HTTP请求处理中间件
    """

    @staticmethod
    def init_http_filter(app, context):
        @app.middleware("http")
        async def http_middleware(request: Request, call_next: Callable) -> Response:
            handler = HttpHandler()
            return await handler.dispatch(request, call_next)

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        # 检查路由处理函数是否有 no_logging 标记
        route_handler = request.scope.get("route", None)
        if route_handler and route_handler.endpoint:
            if getattr(route_handler.endpoint, 'no_logging', False):
                request.state.no_logging = True
                return await call_next(request)

        # 正常的日志记录流程
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time

        # 只有在未标记 no_logging 的情况下才记录日志
        if not getattr(request.state, 'no_logging', False):
            await self._log_request(request, process_time)
        
        return response

    async def _log_request(self, request: Request, process_time: float):
        """
        记录请求日志
        """
        # 获取请求头信息
        headers = dict(request.headers)
        # 移除敏感信息
        if "authorization" in headers:
            headers["authorization"] = "***"

        # 获取请求体
        body = {}
        if hasattr(request.state, "json_body"):
            body = request.state.json_body

        # 构建日志信息
        log_info = {
            "method": request.method,
            "path": request.url.path,
            "client_ip": request.client.host if request.client else None,
            "headers": headers,
            "json_body": body
        }

        # 记录请求信息
        # logger.info("\n" + str(log_info))
        # logger.info(f"[Request Process_time]: {process_time} second.")
        # logger.info(f'{request.client.host}:{request.client.port} - "{request.method} {request.url.path} HTTP/1.1" {200}')