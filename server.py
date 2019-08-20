# -*- coding: utf-8 -*-

"""
@author: Jim
@project: tornado_learning
@time: 2019/8/19 11:18
@desc:
"""

from __future__ import annotations

import wtforms_json
from peewee_async import Manager
from tornado import web, ioloop

from tornado_learning.settings import database
from tornado_learning.settings import settings
from tornado_learning.urls import urlpattern


def make_app():
    app = web.Application(urlpattern, **settings)

    # 就在这里添加数据库连接
    objects = Manager(database)

    # 禁止使用同步操作
    database.set_allow_sync(False)
    app.objects = objects
    return app


if __name__ == '__main__':
    wtforms_json.init()

    app = make_app()

    app.listen(8888)
    ioloop.IOLoop.current().start()
