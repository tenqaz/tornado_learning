# -*- coding: utf-8 -*-

"""
@author: Jim
@project: tornado_learning
@time: 2019/8/19 11:32
@desc:
"""

from __future__ import annotations
from apps.school.handler import StudentHandler, StudentFormHandler, TeacherHandler

urlpattern = [
    (r"/student", StudentHandler),
    (r"/studentForm", StudentFormHandler),
    (r"/teacher", TeacherHandler)
]
