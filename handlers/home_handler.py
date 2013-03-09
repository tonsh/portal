#coding=utf-8
''' 首页 '''

import tornado.web
from handlers.base_handler import BaseHandler

class HomeHandler(BaseHandler):
    ''' 首页 '''
    def get(self):
        self.render("home.html")
