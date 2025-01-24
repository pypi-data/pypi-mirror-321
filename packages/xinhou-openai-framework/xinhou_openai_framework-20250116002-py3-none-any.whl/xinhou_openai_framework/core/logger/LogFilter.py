from functools import wraps
from starlette.requests import Request


class NoLogging:
    """
    装饰器类，用于禁用特定接口的日志输出
    使用方法:
    @NoLogging()
    @app.get("/path")
    async def endpoint():
        pass
    """
    def __init__(self):
        self.no_logging = True

    def __call__(self, func):
        setattr(func, 'no_logging', self.no_logging)
        
        @wraps(func)
        async def wrapper(*args, **kwargs):
            request = None
            for arg in args:
                if isinstance(arg, Request):
                    request = arg
                    break
            if request:
                request.state.no_logging = True
            return await func(*args, **kwargs)
        setattr(wrapper, 'no_logging', self.no_logging)
        return wrapper