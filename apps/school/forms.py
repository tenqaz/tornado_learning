# -*- coding: utf-8 -*-

"""
@author: Jim
@project: tornado_learning
@time: 2019/8/19 11:32
@desc:
"""

from __future__ import annotations

from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import DataRequired
from wtforms_tornado import Form


class StudentForm(Form):
    """
    可以作为student的 post 和 put 的表单使用。
    """

    id = IntegerField("id", null=True)
    name = StringField("姓名", validators=[DataRequired("请输入姓名")])
    age = IntegerField("年龄", validators=[DataRequired("请输入年龄")])
    desc = TextAreaField("个人简介", validators=[DataRequired("请输入个人简介")])


class TeacherForm(Form):
    student_id = IntegerField("学生id")
    name = StringField("姓名", validators=[DataRequired("请输入姓名")])
    age = IntegerField("年龄", validators=[DataRequired("请输入年龄")])
    subject = TextAreaField("学科", validators=[DataRequired("请输入学科")])
