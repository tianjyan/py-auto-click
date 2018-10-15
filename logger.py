# !/usr/bin/python
# -*- coding: utf-8 -*-
# pylint: disable = C0103

import os
import logging
from logging.handlers import RotatingFileHandler
from logging import StreamHandler

__author__ = 'Tianjie Yang'
__email__ = "tianjyan@qq.com"

class Logger(object):
    """
    Global config for Logger
    """
    LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
    LOG_DEBUG = 'debug.log'
    LOG_INFO = 'info.log'
    LOG_WARNING = 'warning.log'
    LOG_ERROR = 'error.log'
    LOG_FOLDER = 'logs'
    logger = None

    def __init__(self):
        base = os.path.join(os.getcwd(), self.LOG_FOLDER)
        if not os.path.exists(base):
            os.mkdir(base)
        self.debugLogger = self.initlogger(logging.DEBUG, self.LOG_DEBUG)
        self.infoLogger = self.initlogger(logging.INFO, self.LOG_INFO)
        self.warningLogger = self.initlogger(logging.WARNING, self.LOG_WARNING)
        self.errorLogger = self.initlogger(logging.ERROR, self.LOG_ERROR)

    def debug(self, msg):
        """
        Output debug msg to file
        """
        self.debugLogger.debug(msg)

    def info(self, msg):
        """
        Output info msg to file
        """
        self.infoLogger.info(msg)

    def warning(self, msg):
        """
        Output waring msg to file
        """
        self.warningLogger.warning(msg)

    def error(self, msg):
        """
        Output error msg to file
        """
        self.errorLogger.error(msg)

    def initlogger(self, level, name):
        """
        init logger
        """
        cwd = os.getcwd()
        formatter = logging.Formatter(self.LOG_FORMAT)
        logger = logging.getLogger(name)
        logger.setLevel(level)
        fh = RotatingFileHandler(os.path.join(cwd, self.LOG_FOLDER, name),
                                 maxBytes=10 * 1024 * 1024,
                                 backupCount=5)
        fh.setFormatter(formatter)
        fh.setLevel(level)
        logger.addHandler(fh)
        if level is not logging.DEBUG:
            ch = StreamHandler()
            ch.setFormatter(formatter)
            ch.setLevel(level)
            logger.addHandler(ch)
        return logger