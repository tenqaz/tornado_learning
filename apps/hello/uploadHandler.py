# -*- coding: utf-8 -*-

"""
@author: Jim
@project: tornado_learning
@time: 2019/8/20 14:48
@desc:
    上传文件
"""

from __future__ import annotations

from tornado_learning.handler import BaseHandler
import os
import uuid
import aiofiles


class UploadHandler(BaseHandler):

    async def post(self):
        ret_data = {}

        files_meta = self.request.files.get("front_image", None)
        if not files_meta:
            self.set_status(400)
            ret_data["front_image"] = "请上传图片"
        else:
            for meta in files_meta:
                filename = meta["filename"]
                new_filename = "{uuid}_{filename}".format(uuid=uuid.uuid1(), filename=filename)
                file_path = os.path.join(self.settings["MEDIA_ROOT"], new_filename)

                async with aiofiles.open(file_path, "wb") as f:
                    await f.write(meta["body"])

                ret_data['file_path'] = file_path

        return self.finish(ret_data)
