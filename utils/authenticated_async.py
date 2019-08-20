# -*- coding: utf-8 -*-

"""
@author: Jim
@project: tornado_learning
@time: 2019/8/20 12:16
@desc:
"""

from __future__ import annotations

import jwt

from apps.user.models import User


def authenticated_async(method):
    async def wrapper(self, *args, **kwargs):

        # ret_data = {}

        tsessionid = self.request.headers.get("tsessionid", None)
        if tsessionid:

            try:
                payload = jwt.decode(tsessionid, self.settings["secret_key"], leeway=self.settings["jwt_expire"],
                                     options={"verify_exp": True})

                user_id = payload["id"]
                try:
                    user = await self.application.objects.get(User, id=user_id)
                    self._current_user = user
                    await method(self, *args, **kwargs)
                except User.DoesNotExist as e:
                    self.set_status(401)
            except jwt.ExpiredSignatureError as e:
                self.set_status(401)

    return wrapper
