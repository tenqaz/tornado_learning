# -*- coding: utf-8 -*-

"""
@author: Jim
@project: tornado_learning
@time: 2019/8/19 14:36
@desc:

finish 和 write的区别。

"""

from __future__ import annotations

from tornado_learning.handler import BaseHandler

import time


class Write_Finish_Handler(BaseHandler):

    def get(self):
        self.write("hello")
        time.sleep(4)
        self.finish("world")


class Finish_Write_Handler(BaseHandler):

    def get(self):
        self.finish("hello")
        self.write("world")
