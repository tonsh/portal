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

class ListHandler(BaseHandler):
    def get(self):
        params = {
            'categories': Category().reget_children(),
        }
        self.return_json(params)

class AddHandler(BaseHandler):
    ''' 添加分类 '''
    def get(self):
        params = {
            'categories': Category().get_children(),
        }
        self.render("admin/category/add.html", **params)

    def post(self):
        try:
            args = self.request_args()
            category = Category().insert(args)
            self.redirect("/admin/category")
        except FormError as error:
            self.return_json(error.msg)
        except ForbiddenError as error:
            raise tornado.web.HTTPError(403)
