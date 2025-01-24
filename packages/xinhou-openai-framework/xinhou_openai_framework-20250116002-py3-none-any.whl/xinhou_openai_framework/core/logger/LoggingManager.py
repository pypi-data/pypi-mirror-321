import logging
import os
import sys
from datetime import datetime
from logging import Formatter
from traceback import format_exception

from loguru import logger as loguru_logger
from starlette.requests import Request


class InterceptHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        self.formatter = Formatter(
            '%(asctime)s | %(levelname)s | %(name)s:%(funcName)s:%(lineno)d | %(message)s'
        )

    def emit(self, record):
        # 避免处理已经被 loguru 处理过的消息
        if record.name == "loguru" or getattr(record, "_has_been_handled", False):
            return

        # 检查是否是被标记为不需要记录日志的请求
        try:
            if hasattr(record, 'request'):
                request = record.request
                if isinstance(request, Request) and getattr(request.state, 'no_logging', False):
                    return
        except:
            pass

        # 过滤掉 SQL 相关的日志
        try:
            msg_str = str(record.msg)
            if any(pattern in msg_str for pattern in [
                'SELECT',
                'BEGIN',
                'COMMIT',
                'ROLLBACK',
                '[raw sql]'
            ]):
                return
        except:
            pass

        # 标记该记录已被处理
        record._has_been_handled = True

        # 获取对应的 Loguru 级别
        try:
            level = loguru_logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # 找到调用者的文件名和行号
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        # 构造消息
        msg = record.getMessage()
        if record.exc_info:
            exc_type, exc_value, exc_traceback = record.exc_info
            formatted_exception = ''.join(format_exception(exc_type, exc_value, exc_traceback))
            msg += '\n' + formatted_exception

        # 使用 loguru 记录日志
        loguru_logger.opt(depth=depth, exception=record.exc_info).log(level, msg)


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

        # 配置 loguru
        config = {
            "handlers": [
                {
                    "sink": sys.stdout,
                    "format": "<green>{time:YYYY-MM-DD HH:mm:ss,SSS}</green> | <level>{level: <8}</level> | <cyan>{name}:{function}:{line}</cyan> | <level>{message}</level>",
                    "colorize": True,
                    "level": "INFO",
                    "enqueue": True,
                    "backtrace": True,
                    "diagnose": True
                },
                {
                    "sink": file_info,
                    "format": "{time:YYYY-MM-DD HH:mm:ss,SSS} | {level: <8} | {name}:{function}:{line} | {message}",
                    "rotation": "00:00",
                    "retention": "7 days",
                    "compression": "zip",
                    "level": "INFO",
                    "enqueue": True,
                    "backtrace": True,
                    "diagnose": True
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
