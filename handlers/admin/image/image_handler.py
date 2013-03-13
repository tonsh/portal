#coding=utf-8
''' 图片管理后台 '''

import time
import tornado.web
from handlers.base_handler import BaseHandler
from business.category import Category
from business.image import Image
from libs.errors import FormError
from libs.errors import ForbiddenError
from libs.utils import make_file_name

class IndexHandler(BaseHandler):
    ''' 显示图片列表 '''
    def get(self, cid=0):
        params = {
            'categories': Category().reget_children(),
            'current_category': cid,
            'images': Image().get_all_by_category(cid)
        }
        self.render("admin/image/index.html", **params)

class AddHandler(BaseHandler):
    ''' 添加图片 '''
    def get(self):
        params = {
            'categories': Category().reget_children(1),
        }
        self.render("admin/image/add.html", **params)

    def post(self):
        try:
            image = self.request.files['image'][0]
            # 时间戳精确到毫秒作为文件名
            extension = image['filename'].split('.')[-1]
            src_image = make_file_name(extension)

            file_obj = open(src_image, 'wb')
            file_obj.write(image['body'])
            file_obj.close()

            args = self.request_args()
            args['image'] = src_image
            image = Image().insert(args)
            self.return_json({"success": True})
        except FormError as error:
            self.return_json(error.msg)
        except ForbiddenError as error:
            raise tornado.web.HTTPError(403)
