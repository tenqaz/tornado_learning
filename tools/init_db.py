# -*- coding: utf-8 -*-

"""
@author: Jim
@project: tornado_learning
@time: 2019/8/19 11:43
@desc:
"""

from __future__ import annotations

from tornado_learning.settings import database
from apps.school.models import Student, Teacher
from apps.user.models import User


def init_db():
    database.create_tables([Student, Teacher, User])


if __name__ == '__main__':
    init_db()
