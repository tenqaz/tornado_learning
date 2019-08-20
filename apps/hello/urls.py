# -*- coding: utf-8 -*-

"""
@author: Jim
@project: tornado_learning
@time: 2019/8/19 14:36
@desc:
"""

from __future__ import annotations

from apps.hello.write_finish_handler import Write_Finish_Handler, Finish_Write_Handler
from apps.hello.uploadHandler import UploadHandler


urlpattern = [
    (r"/write_finish_handler", Write_Finish_Handler),
    (r"/finish_write_handler", Finish_Write_Handler),
    (r"/upload", UploadHandler)
]
