# -*- coding: utf-8 -*-

"""
@author: Jim
@project: tornado_learning
@time: 2019/8/19 11:20
@desc:
"""

from __future__ import annotations

from apps.hello.handler import HelloHandler
from apps.school.urls import urlpattern as school_urls
from apps.hello.urls import urlpattern as hello_urls
from apps.user.urls import urlpattern as user_urls

urlpattern = [
    (r"/hello", HelloHandler)
]

urlpattern += school_urls
urlpattern += hello_urls
urlpattern += user_urls
