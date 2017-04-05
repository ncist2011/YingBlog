#!/usr/bin/env python3.5

import os
import sys
import time

from tornado.ioloop import IOLoop
import tornado.web
from tornado.options import define, options

define('port', default=8080, help="listen on given port", type=int)

rootpath = os.path.dirname(__file__)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect('/login')

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('login.html')


settings = {'static_path' : os.path.join(rootpath, 'static/'),
           'template_path': os.path.join(rootpath,'static/template/'),
           'login_url': '/login'}

application = tornado.web.Application([
    (r'/', IndexHandler),
    (r'/login', LoginHandler),
    ], **settings
)

if __name__ == "__main__":
    application.listen(options.port)
    IOLoop.instance().start()
