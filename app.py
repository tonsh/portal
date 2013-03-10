#coding=utf-8
''' server application '''

import tornado.web
import tornado.ioloop
import models
from settings import STATIC_DIR
from settings import LOCALE_DIR
from handlers.home_handler import HomeHandler
from handlers.admin_handler import AdminHandler

settings = {
    'static_path': STATIC_DIR,
    'cookie_secret': 'c5586ff9f6ac5211198e37c46154b26e',
    'xsrf_cookies': True,
}


application = tornado.web.Application([
    (r'/', HomeHandler),
    (r'/admin', AdminHandler),
], **settings)


if __name__ == '__main__':
    models.create_db()
    tornado.locale.load_gettext_translations(LOCALE_DIR, 'lang')

    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
