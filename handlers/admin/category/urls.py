#coding=utf-8

from handlers.admin.category.category_handler import IndexHandler
from handlers.admin.category.category_handler import DeleteHandler
from handlers.admin.category.category_handler import AddHandler

_urls = [
    (r'/admin/category', IndexHandler),
    (r'/admin/category/delete/([0-9]+)', DeleteHandler),
    (r'/admin/category/add', AddHandler),
]
