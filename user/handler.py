#!/usr/bin/env python3.5
# coding=utf-8

import tornado.web
import json
from mongo.mongod import Connection
from base.handler import BaseHandler

class IndexHandler(BaseHandler):
    def get(self):
        self.redirect("/login")

class LoginHandler(BaseHandler):
    def get(self):
        if not self.get_current_user():
            self.render("login.html")
        else:
            self.redirect("/home")

    def post(self):
        username = self.get_argument(username, "")
        passwd = self.get_argument(passwd, "")

        meta = {'username': username,
                'passwd': passwd}

        collection = 'user'
        user = yield Connection.get_document(dc, meta)

        if not user:
            self.write("error username or passwd")
        else:
            self.set_secure_cookie('userid', username, expires_days=None ,httponly=True)
            self.write(json.dumps({'next': self.get_argument('next', '/')}))
            self.flush()

class LogoutHandler(BaseHandler):
    def post(self):
        self.clear_all_cookies()
        self.redirect('/')
