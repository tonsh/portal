#coding=utf-8
''' 管理后台 '''

import tornado.web
from handlers.base_handler import BaseHandler

class AdminHandler(BaseHandler):
    ''' 管理后台 '''
    def get(self):
        self.render("admin.html")
