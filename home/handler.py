#!/usr/bin/env python3.5
# encoding: utf-8

from base.handler import BaseHandler

class HomeBaseHandler(BaseHandler):
    def get(self):
        self.render('homebase.html')
