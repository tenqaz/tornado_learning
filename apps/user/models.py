# -*- coding: utf-8 -*-

"""
@author: Jim
@project: tornado_learning
@time: 2019/8/19 17:35
@desc:
"""

from __future__ import annotations

from tornado_learning.models import BaseModel
from peewee import CharField, BlobField
from bcrypt import hashpw, gensalt


class PasswordHash(bytes):
    def check_password(self, password):
        """
        比较传入的密码和数据库中的密码是否匹配
        :param password:
        :return:
        """
        password = password.encode('utf-8')
        return hashpw(password, self) == self


class PasswordField(BlobField):
    def __init__(self, iterations=12, *args, **kwargs):
        if None in (hashpw, gensalt):
            raise ValueError('Missing library required for PasswordField: bcrypt')
        self.bcrypt_iterations = iterations
        self.raw_password = None
        super(PasswordField, self).__init__(*args, **kwargs)

    def db_value(self, value):
        """
        将python的值转换成存入数据库的值
        存入数据库的值，是通过bcrypt加密后的密文。
        :param value:
        :return:
        """
        if isinstance(value, PasswordHash):
            return bytes(value)

        if isinstance(value, str):
            value = value.encode('utf-8')
        salt = gensalt(self.bcrypt_iterations)
        return value if value is None else hashpw(value, salt)

    def python_value(self, value):
        """
        将数据库中的值转换成python中的值
        这个值是一个PasswordHash对象。该对象提供比较密码的方法。
        :param value:
        :return:
        """
        if isinstance(value, str):
            value = value.encode('utf-8')

        return PasswordHash(value)


class User(BaseModel):
    username = CharField(max_length=16, verbose_name="用户名", index=True, unique=True)
    password = PasswordField(verbose_name="密码")
    address = CharField(max_length=200, null=True, verbose_name="地址")
