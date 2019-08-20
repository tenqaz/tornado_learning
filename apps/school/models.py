# -*- coding: utf-8 -*-

"""
@author: Jim
@project: tornado_learning
@time: 2019/8/19 11:32
@desc:
"""

from __future__ import annotations

from peewee import CharField, IntegerField, TextField, ForeignKeyField

from tornado_learning.models import BaseModel


class Student(BaseModel):
    name = CharField(max_length=100, null=False, verbose_name="学生名")
    age = IntegerField(null=False, verbose_name="年龄")
    desc = TextField(verbose_name="个人简介")


class Teacher(BaseModel):
    student = ForeignKeyField(rel_model=Student, related_name="teachers")
    name = CharField(max_length=100, null=False, verbose_name="老师名")
    age = IntegerField(null=False, verbose_name="年龄")
    subject = CharField(max_length=100, null=False, verbose_name="学科")

    @classmethod
    def extend(cls):
        return cls.select(cls, Student.name, Student.age).join(Student)
