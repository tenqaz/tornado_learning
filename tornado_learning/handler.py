# -*- coding: utf-8 -*-

"""
@author: Jim
@project: tornado_learning
@time: 2019/8/19 11:23
@desc:
"""

from __future__ import annotations

from tornado.web import RequestHandler


class BaseHandler(RequestHandler):
    """
    通用的request请求。
    在每次请求前添加头信息。
    """

    def set_default_headers(self):
        # 允许跨域
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', 'x-requested-with')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, DELETE, PUT, PATCH, OPTIONS')
