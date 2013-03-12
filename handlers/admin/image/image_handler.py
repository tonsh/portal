#coding=utf-8
''' 图片管理后台 '''

import tornado.web
from handlers.base_handler import BaseHandler
from business.category import Category
from business.image import Image
from libs.errors import FormError
from libs.errors import ForbiddenError

class IndexHandler(BaseHandler):
    ''' 显示图片列表 '''
    def get(self, cid=0):
        params = {
            'categories': Category().reget_children(),
            'current_category': cid,
            'images': Image().get_all_by_category(cid)
        }
        self.render("admin/category/index.html", **params)

class AddHandler(BaseHandler):
    ''' 添加图片 '''
