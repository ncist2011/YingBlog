#!/usr/bin/env python3.5
# encoding: utf-8

import tornado.web
from base.handler import BaseHandler

class HomeBaseHandler(BaseHandler):
    def get(self):
        self.render('home.html')

class HomeEntry(tornado.web.UIModule):
    def render(self):
        self.render('entry.html')
