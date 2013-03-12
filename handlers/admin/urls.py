#coding=utf-8

from handlers.admin.admin_handler import IndexHandler
from handlers.admin.category.urls import _urls as category_urls
from handlers.admin.image.urls import _urls as image_urls

_urls = [
    (r'/admin', IndexHandler),
] + category_urls + image_urls
