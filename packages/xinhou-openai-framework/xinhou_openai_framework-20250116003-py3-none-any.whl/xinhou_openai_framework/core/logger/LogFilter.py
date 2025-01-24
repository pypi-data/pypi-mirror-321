from functools import wraps
from starlette.requests import Request
from loguru import logger
import logging
import sys


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
                # 设置请求级别的日志禁用标志
                request.state.no_logging = True
                
                # 禁用所有日志
                logger.remove()  # 移除所有日志处理器
                logging.disable(logging.CRITICAL)  # 禁用标准库日志
                
                try:
                    result = await func(*args, **kwargs)
                finally:
                    # 重新启用日志
                    logger.add(sys.stderr, level="INFO")  # 重新添加日志处理器
                    logging.disable(logging.NOTSET)  # 重新启用标准库日志
                
                return result
            else:
                return await func(*args, **kwargs)
                
        setattr(wrapper, 'no_logging', self.no_logging)
        return wrapper