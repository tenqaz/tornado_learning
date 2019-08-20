# -*- coding: utf-8 -*-

"""
@author: Jim
@project: tornado_learning
@time: 2019/8/19 11:20
@desc:
"""

from __future__ import annotations

import peewee_async
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

settings = {
    "debug": True,
    "template_path": "templates",
    "secret_key": "ZGGA#Mp4yL4w5CDa",
    "jwt_expire": 7*24*3600,
    "MEDIA_ROOT": os.path.join(BASE_DIR, "media"),
}

database = peewee_async.MySQLDatabase(
    'tornado_learning', host="127.0.0.1", port=3306, user="root", password="root1234"
)