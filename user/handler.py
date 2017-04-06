#!/usr/bin/env python3.5
# coding=utf-8

import tornado.web
from mongo.mongod import Connection

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect("/login")

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        if not self.current_user:
            self.render("login.html")

    def post(self):
        username = self.get_argument(username, "")
        passwd = self.get_argument(passwd, "")

        meta = {'username': username,
                'passwd': passwd}

        coll = 'user'
        user = yield Connection.get_document(coll, meta)

        if not user:
            print(1111111111111111111111111111)


class LogoutHandler(tornado.web.RequestHandler):
    def post(self):
        self.render("login.html")