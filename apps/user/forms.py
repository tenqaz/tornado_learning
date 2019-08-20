# -*- coding: utf-8 -*-

"""
@author: Jim
@project: tornado_learning
@time: 2019/8/19 17:35
@desc:
"""

from __future__ import annotations

from wtforms_tornado import Form
from wtforms import StringField, TextAreaField


class LoginForm(Form):
    username = StringField("用户名")
    password = StringField("密码")

class RegisterForm(LoginForm):
    address = TextAreaField("地址")
