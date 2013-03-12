#coding=utf-8
''' 分类管理后台 '''

import tornado.web
from handlers.base_handler import BaseHandler
from business.category import Category
from libs.errors import FormError
from libs.errors import ForbiddenError

class IndexHandler(BaseHandler):
    ''' 显示分类列表 '''
    def get(self):
        params = {
            'categories': Category().reget_children(),
        }
        self.render("admin/category/index.html", **params)
