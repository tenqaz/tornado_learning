# -*- coding: utf-8 -*-

"""
@author: Jim
@project: tornado_learning
@time: 2019/8/19 17:35
@desc:
"""

from __future__ import annotations

from apps.user.handler import LoginHandler, RegisterHandler

urlpattern = [
    (r"/login", LoginHandler),
    (r"/register", RegisterHandler)
]
