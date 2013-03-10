#coding=utf-8

from handlers.admin_handler import AdminHandler
from handlers.admin.category.urls import _urls as cat_urls

_urls = [
    (r'/admin', AdminHandler),
] + cat_urls
