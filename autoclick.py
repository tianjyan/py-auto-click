# !/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time
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
            self.revisit(0, 500)

    def revisit(self, x, y):
        os.system(u'adb shell input tap {} {}'.format(x, y))
        time.sleep(3)
        os.system(u'adb shell input tap {} {}'.format(1000, 1800))
        time.sleep(3)
        os.system(u'adb shell input tap {} {}'.format(420, 350))
        os.system(u'adb shell input tap {} {}'.format(900, 1100))
        os.system(u'adb shell input tap {} {}'.format(1020, 1150))
        os.system(u'adb shell input tap {} {}'.format(1000, 1800))
        os.system(u'adb shell input keyevent 4')
        time.sleep(3)

if __name__ == "__main__":
    logger = Logger()
    autoClick = AutoClick(logger)
    autoClick.run()