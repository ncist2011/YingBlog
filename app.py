#!/usr/bin/env python3.5

import os
import sys
import time

from tornado.ioloop import IOLoop
import tornado.web
import tornado.httpserver
from tornado.options import define, options
from urlmap import urls
from home.handler import HomeEntry

define('port', default=8080, help="listen on given port", type=int)

rootpath = os.path.dirname(__file__)

settings = {'static_path' : os.path.join(rootpath, 'static/'),
            'template_path': os.path.join(rootpath, 'static/template'),
           'xsrf_cookies': True,
           'ui_modules' :{'Entry': HomeEntry},
           'cookie_secret': "cXzLGhX5SlGe+Bm+DgdiqECKjyXEeED2pzaOnUttCtM=",
           'login_url': '/login'}

application = tornado.web.Application(
    handlers=urls,
    **settings
)

if __name__ == "__main__":
    httpserver = tornado.httpserver.HTTPServer(application)
    httpserver.listen(options.port)
    IOLoop.instance().start()
