# -*- coding: utf-8 -*-

"""
@author: Jim
@project: tornado_learning
@time: 2019/8/19 11:33
@desc:
"""

from __future__ import annotations

from datetime import datetime

from peewee import Model, DateTimeField

from tornado_learning.settings import database


class BaseModel(Model):
    create_time = DateTimeField(default=datetime.now, verbose_name="创建时间")

    class Meta:
        database = database
