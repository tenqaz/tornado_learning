# -*- coding: utf-8 -*-

"""
@author: Jim
@project: tornado_learning
@time: 2019/8/19 11:23
@desc:
"""

from __future__ import annotations

from tornado_learning.handler import BaseHandler


class HelloHandler(BaseHandler):
    """
        hello tornado
    """

    def get(self):
        self.write("hello tornado")

        return self.finish()