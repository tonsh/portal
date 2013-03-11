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

class DeleteHandler(BaseHandler):
    def get(self, cid):
        Category().delete(cid)
        self.return_json({'success': True})

class AddHandler(BaseHandler):
    ''' 添加分类 '''
    def get(self):
        params = {
            'categories': Category().reget_children(),
        }
        self.render("admin/category/add.html", **params)

    def post(self):
        try:
            args = self.request_args()
            category = Category().insert(args)
            #self.redirect("/admin/category")
            self.return_json({"success": True})
        except FormError as error:
            self.return_json(error.msg)
        except ForbiddenError as error:
            raise tornado.web.HTTPError(403)
