# !/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.append("..")
import time
from abcadb import ABCAdb
from logger import Logger

__author__ = 'Tianjie Yang'
__email__ = "tianjyan@qq.com"

class AutoClick(ABCAdb):

    def run(self):
        while True:
            self.revisit(200, 715)
            self.swipe(0, 1200, 0, 975)
            time.sleep(2)

    def revisit(self, x, y):
        # 点击客户
        self.tap(x, y)
        # 等待客户信息加载完成
        time.sleep(3)
        # 点击回访
        self.tap(1000, 500)
        # 等待对话框弹出
        time.sleep(1)
        # 输入回访文本
        self.text(u'考虑')
        # 确认回访内容
        self.tap(300, 1150)
         # 等待对话框消失
        time.sleep(1)
        # 返回主页面
        self.goback()
         # 等待返回
        time.sleep(1)

if __name__ == "__main__":
    logger = Logger()
    autoClick = AutoClick(logger)
    autoClick.run()