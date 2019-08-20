# -*- coding: utf-8 -*-

"""
@author: Jim
@project: tornado_learning
@time: 2019/8/19 17:35
@desc:
"""

from __future__ import annotations

from datetime import datetime

import jwt

from apps.user.forms import LoginForm, RegisterForm
from apps.user.models import User
from tornado_learning.handler import BaseHandler


class LoginHandler(BaseHandler):

    async def post(self):

        # 返回的数据
        ret_data = {}

        loginForm = LoginForm(self.request.arguments)
        if loginForm.validate():
            username = loginForm.username.data
            password = loginForm.password.data

            try:

                user = await self.application.objects.get(User, username=username)
                if not user.password.check_password(password):
                    # 密码验证错误

                    self.set_status(400)
                    ret_data['non_fields'] = "用户名或密码错误"
                else:
                    # 登录成功
                    # 生成json web token
                    payload = {
                        "id": user.id,
                        "username": user.username,
                        "exp": datetime.now()
                    }
                    token = jwt.encode(payload, self.settings['secret_key'], algorithm='HS256')
                    ret_data['username'] = user.username
                    ret_data['token'] = token.decode("utf8")
            except User.DoesNotExist as e:
                self.set_status(400)
                ret_data["mobile"] = "用户不存在"

        return self.finish(ret_data)


class RegisterHandler(BaseHandler):

    async def post(self):

        ret_data = {}

        registerForm = RegisterForm(self.request.arguments)
        if registerForm.validate():
            username = registerForm.username.data

            try:
                exist_user = await self.application.objects.get(User, username=username)
                ret_data["username"] = "用户名已经存在"
            except User.DoesNotExist as e:
                user = await self.application.objects.create(User, **registerForm.data)
                ret_data["id"] = user.id
        else:
            self.set_status(400)
            for field in registerForm.erros:
                ret_data[field] = registerForm[field][0]

        return self.finish(ret_data)
