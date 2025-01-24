import logging
import os
from datetime import datetime
from logging import StreamHandler
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
import sys

from loguru import logger as loguru_logger

from xinhou_openai_framework.core.logger.InterceptHandler import InterceptHandler


class LoggingManager:
    @staticmethod
    def init_logger(app, log_path: str = None):
        """
        初始化 logger，将日志同时输出到 console 和指定的文件中。
        """
        if log_path is None:
            return

        # 确保日志目录存在
        os.makedirs(log_path, exist_ok=True)

        # 生成当天的日志文件路径
        file_info = os.path.join(log_path, f"{datetime.now().strftime('%Y-%m-%d')}.log")

        # 移除所有已存在的处理器
        loguru_logger.remove()
        
        # 添加日志过滤器
        def log_filter(record):
            try:
                if hasattr(record["extra"], "request"):
                    request = record["extra"]["request"]
                    return not getattr(request.state, "no_logging", False)
            except:
                pass
            return True

        # 配置 loguru
        config = {
            "handlers": [
                {
                    "sink": sys.stdout,
                    "filter": log_filter,
                    "format": "<green>{time:YYYY-MM-DD HH:mm:ss,SSS}</green> | <level>{level: <8}</level> | <cyan>{name}:{function}:{line}</cyan> | <level>{message}</level>",
                    "colorize": True,
                    "level": "INFO"
                },
                {
                    "sink": file_info,
                    "filter": log_filter,
                    "format": "{time:YYYY-MM-DD HH:mm:ss,SSS} | {level: <8} | {name}:{function}:{line} | {message}",
                    "rotation": "00:00",
                    "retention": "7 days",
                    "compression": "zip",
                    "level": "INFO"
                }
            ]
        }

        # 应用 loguru 配置
        for handler in config["handlers"]:
            loguru_logger.add(**handler)

        # 替换特定模块的日志配置
        for _log in [
            'uvicorn', 
            'uvicorn.error', 
            'uvicorn.access', 
            'sqlalchemy.engine',
            'HttpHandler',
            'InitializeHandler',
            'nacos.client',
            'apps',
        ]:
            _logger = logging.getLogger(_log)
            _logger.handlers = []  # 清除所有处理器
            _logger.addHandler(InterceptHandler())
            _logger.propagate = False  # 防止日志传播

        # 配置根日志记录器
        root_logger = logging.getLogger()
        root_logger.handlers = []  # 清除所有处理器
        root_logger.addHandler(InterceptHandler())
        root_logger.setLevel(logging.INFO)

    @staticmethod
    def init_custom_logger(name, file_info):
        """
        为特定模块初始化日志处理器
        """
        custom_logger = logging.getLogger(name)
        custom_logger.handlers = []  # 清除所有处理器
        custom_logger.addHandler(InterceptHandler())
        custom_logger.propagate = False  # 防止日志传播
