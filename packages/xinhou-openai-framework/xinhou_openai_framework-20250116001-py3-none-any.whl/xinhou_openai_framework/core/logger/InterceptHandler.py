import logging
import os
import sys
from datetime import datetime
from logging import StreamHandler, Formatter
from logging.handlers import RotatingFileHandler
from traceback import format_exception

from loguru import logger as loguru_logger


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

        # 过滤掉 GET 请求和 SQL 相关的日志
        try:
            msg_str = str(record.msg)
            # 过滤掉 GET 请求日志
            if '"method": "GET"' in msg_str or 'GET /' in msg_str:
                return
            # 过滤掉 SQL 相关日志
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