# !/usr/bin/python
# -*- coding: utf-8 -*-

import os
from logger import Logger

__author__ = 'Tianjie Yang'
__email__ = "tianjyan@qq.com"

class AutoClick:
    logger = None
    """
    Usage: run method `run` will send events to connected android device.
    """
    def __init__(self, logger):
        self.logger = logger

    def run(self):
        while True:
            self.revisit(500, 500)

    def revisit(self, x, y):
        os.system(u'adb shell input tap {} {}'.format(x, y))
        os.system(u'adb shell input tap {} {}'.format(100, 100))

if __name__ == "__main__":
    logger = Logger()
    autoClick = AutoClick(logger)
    autoClick.run()