#coding=utf-8

from handlers.admin.image.image_handler import IndexHandler
from handlers.admin.image.image_handler import AddHandler

_urls = [
    (r'/admin/image', IndexHandler),
    (r'/admin/image/add', AddHandler),
]
