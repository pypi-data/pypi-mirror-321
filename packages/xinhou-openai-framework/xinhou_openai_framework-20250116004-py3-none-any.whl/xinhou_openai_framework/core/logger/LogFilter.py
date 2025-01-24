from functools import wraps
from starlette.requests import Request
from loguru import logger
import logging
import sys
from contextvars import ContextVar

# 使用上下文变量来存储原始的日志级别
_original_log_levels = ContextVar('original_log_levels', default={})

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
                # 保存原始日志级别
                original_levels = {
                    'sqlalchemy': logging.getLogger('sqlalchemy').level,
                    'sqlalchemy.engine': logging.getLogger('sqlalchemy.engine').level,
                    'root': logging.getLogger().level
                }
                _original_log_levels.set(original_levels)
                
                # 禁用所有日志
                logging.getLogger('sqlalchemy').setLevel(logging.CRITICAL)
                logging.getLogger('sqlalchemy.engine').setLevel(logging.CRITICAL)
                logging.getLogger().setLevel(logging.CRITICAL)
                
                try:
                    result = await func(*args, **kwargs)
                finally:
                    # 恢复原始日志级别
                    original_levels = _original_log_levels.get()
                    logging.getLogger('sqlalchemy').setLevel(original_levels['sqlalchemy'])
                    logging.getLogger('sqlalchemy.engine').setLevel(original_levels['sqlalchemy.engine'])
                    logging.getLogger().setLevel(original_levels['root'])
                
                return result
            else:
                return await func(*args, **kwargs)
                
        setattr(wrapper, 'no_logging', self.no_logging)
        return wrapper