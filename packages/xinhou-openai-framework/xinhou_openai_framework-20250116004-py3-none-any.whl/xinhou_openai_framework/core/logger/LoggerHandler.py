# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
全局日志初始化代理类
----------------------------------------------------
@Project :   xinhou-openai-framework
@File    :   LoggerHandler.py
@Contact :   sp_hrz@qq.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/18 18:37   shenpeng   1.0         None
"""
import logging
import logging.config
import os
import sys

from loguru import logger

from xinhou_openai_framework.core.contents.AppContents import AppContents
from xinhou_openai_framework.core.logger.LoggerManager import LoggingManager


class LoggerHandler:
    """
    日志处理类
    """

    @staticmethod
    def init_logs(app, context):
        # 创建一个自定义的日志过滤器
        class SQLAlchemyFilter(logging.Filter):
            def filter(self, record):
                return not record.name.startswith('sqlalchemy')

        # 完全禁用sqlalchemy的所有日志
        logging.getLogger('sqlalchemy').handlers = []
        logging.getLogger('sqlalchemy').propagate = False
        logging.getLogger('sqlalchemy').disabled = True

        # 禁用所有sqlalchemy相关模块的日志
        for logger_name in [
            'sqlalchemy',
            'sqlalchemy.engine',
            'sqlalchemy.engine.Engine',
            'sqlalchemy.dialects',
            'sqlalchemy.pool',
            'sqlalchemy.orm',
            'sqlalchemy.engine.base'
        ]:
            log = logging.getLogger(logger_name)
            log.disabled = True
            log.propagate = False
            log.handlers = []

        # 为根日志记录器添加过滤器
        root_logger = logging.getLogger()
        root_logger.addFilter(SQLAlchemyFilter())

        # 配置loguru
        logger.configure(
            handlers=[
                {
                    "sink": sys.stdout,
                    "filter": lambda record: not record["message"].startswith("[SQL]")
                }
            ]
        )

        @app.on_event("startup")
        async def startup_logger_manager_event():
            if context.framework.logging.path is None:
                LoggingManager.init_logger(app, os.path.join(os.getcwd(), AppContents.CTX_INIT_LOGS_DIR))
            else:
                LoggingManager.init_logger(app, os.path.join(os.getcwd(), context.framework.logging.path))
