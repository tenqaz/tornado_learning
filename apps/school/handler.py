# -*- coding: utf-8 -*-

"""
@author: Jim
@project: tornado_learning
@time: 2019/8/19 11:32
@desc:
"""

from __future__ import annotations

import json

import tornado

from apps.school.forms import StudentForm, TeacherForm
from apps.school.models import Student, Teacher
from tornado_learning.handler import BaseHandler
from utils.authenticated_async import authenticated_async


class StudentFormHandler(BaseHandler):

    def get(self):
        studentForm = StudentForm()
        return self.render("student.html", studentForm=studentForm)


class StudentHandler(BaseHandler):

    @authenticated_async
    async def get(self):
        id = self.get_argument("id", None)
        if not id:
            return self.write("please provide the 'id'")

        student = await self.application.objects.get(Student, id=id)

        try:
            self.write({
                "id": student.id,
                "name": student.name
            })
        except Student.DoesNotExist:
            raise tornado.webHttpError(404, "Object not found")

    async def post(self):

        ret_data = {}

        student_form = StudentForm(self.request.arguments)
        if student_form.validate():
            await self.application.objects.create(Student, **student_form.data)

            ret_data["ret"] = "success"
        else:
            for field in student_form.errors:
                ret_data[field] = ret_data.errors[field][0]

        return self.finish(ret_data)

    async def delete(self):
        id = self.get_argument("id", None)
        if not id:
            return self.write("please provide the 'id'")

        student = await self.application.objects.get(Student, id=id)
        await self.application.objects.delete(student)

        self.write("删除成功")

    async def put(self):
        studentForm = StudentForm(self.request.arguments)

        student = Student(**studentForm.data)

        if studentForm.validate():
            await self.application.objects.update(student)
            self.write("更新成功")
        else:
            print(studentForm.errors)


class TeacherHandler(BaseHandler):

    async def get(self):
        ret_data = {"data": []}

        teacher_query = Teacher.extend()
        teacher_query = teacher_query.filter(Teacher.age > 20)
        teachers = await self.application.objects.execute(teacher_query)

        for teacher in teachers:
            item_dict = {
                "teacher_name": teacher.name,
                "teacher_age": teacher.age,
                "student_name": teacher.student.name,
                "student_age": teacher.student.age
            }
            ret_data['data'].append(item_dict)

        return self.finish(ret_data)

    async def post(self):

        ret_data = {}

        param = self.request.body.decode("utf8")
        param = json.loads(param)

        teacherForm = TeacherForm.from_json(param)
        print(teacherForm.data)
        if teacherForm.validate():
            teacher = await self.application.objects.create(Teacher, **teacherForm.data)

            ret_data["ret"] = "success"
        else:
            for field in teacherForm.errors:
                ret_data[field] = teacherForm.errors[field][0]

        return self.finish(ret_data)
