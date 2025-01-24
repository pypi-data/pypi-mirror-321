from functools import wraps

from starlette.requests import Request


class NoLogging:
    """
    装饰器类，用于禁用特定接口的日志输出
    使用方法:
    @app.get("/path")
    @NoLogging()
    async def endpoint():
        pass
    """

    def __call__(self, func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            # 标记该请求不需要记录日志
            request = None
            for arg in args:
                if isinstance(arg, Request):
                    request = arg
                    break
            if request:
                request.state.no_logging = True
            return await func(*args, **kwargs)

        return wrapper
