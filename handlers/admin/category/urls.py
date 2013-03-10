#coding=utf-8

from handlers.admin.category.category_handler import IndexHandler
from handlers.admin.category.category_handler import ListHandler
from handlers.admin.category.category_handler import AddHandler

_urls = [
    (r'/admin/category', IndexHandler),
    (r'/admin/category/list', ListHandler),
    (r'/admin/category/add', AddHandler),
]
