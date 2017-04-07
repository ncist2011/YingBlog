#!/usr/bin/env python3.5
# encoding: utf-8

import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        user_id = self.get_secure_cookie("userid")
        if user_id is None:
            return None
        else:
            return user_id
