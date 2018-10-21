# !/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import time

__author__ = 'Tianjie Yang'
__email__ = "tianjyan@qq.com"

class ABCAdb(object):
    logger = None

    def __init__(self, logger):
        reload(sys)
        sys.setdefaultencoding( "utf-8" )
        self.logger = logger
    
    def tap(self, x, y):
        os.system(u'adb shell input tap {} {}'.format(x, y))

    def swipe(self, sourceX, sourceY, targetX, targetY):
        os.system(u'adb shell input swipe {} {} {} {}'.format(sourceX, sourceY, targetX, targetY))    

    def text(self, str):
        os.system(u'adb shell am broadcast -a ADB_INPUT_B64 --es msg `echo \'{}\' | base64`'.format(str))

    def goback(self):
        os.system(u'adb shell input keyevent 4')
