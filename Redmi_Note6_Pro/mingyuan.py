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
            self.revisit(0, 500)

    def revisit(self, x, y):
        # 点击选择第一个客户
        self.tap(x, y)
        # 等待客户信息加载完成
        time.sleep(3)
        # 点击新增跟进
        self.tap(1000, 2100)
        # 等待新增跟进页面加载完成
        time.sleep(3)
        # 选择跟进方式为去电
        self.tap(420, 350)
        # 点击文本框
        self.tap(100, 1030)
        # 输入内容为回访
        self.text(u'回访')
        # 等待保存按钮可用
        time.sleep(1)
        # 点击保存
        self.tap(1000, 2050)
        # 回退到客户列表
        self.goback()
        # 等待页面刷新完成
        time.sleep(3)

if __name__ == "__main__":
    logger = Logger()
    autoClick = AutoClick(logger)
    autoClick.run()