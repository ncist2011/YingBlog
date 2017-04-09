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
        email = self.get_argument("email", "")
        passwd = self.get_argument("passwd", "")

        meta = {'email': email,
                'passwd': passwd}

        collection = 'user'
        user = Connection.get_document(collection, meta)

        if not user:
            self.write("error email or passwd")
        else:
            self.set_secure_cookie('userid', email, expires_days=None ,httponly=True)
            self.write(json.dumps({'next': self.get_argument('next', '/')}))
            self.flush()

class LogoutHandler(BaseHandler):
    def post(self):
        self.clear_all_cookies()
        self.redirect('/')

class RegisterHandler(BaseHandler):
    def get(self):
        self.render("register.html")

    def post(self):
        username =self.get_argument("username", "")
        email =self.get_argument("email", "")
        passwd =self.get_argument("passwd", "")
