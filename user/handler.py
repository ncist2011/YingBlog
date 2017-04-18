#!/usr/bin/env python3.5
# coding=utf-8

import tornado.web
import json
from mongo.mongod import Connection
from base.handler import BaseHandler
from tornado.gen import coroutine

class IndexHandler(BaseHandler):
    def get(self):
        self.redirect("/login")

class LoginHandler(BaseHandler):
    def get(self):
        if not self.get_current_user():
            self.render("login.html")
        else:
            self.redirect("/home")

    @coroutine
    def post(self):
        email = self.get_argument("email", "")
        passwd = self.get_argument("password", "")
        password = self.encrypt_password(passwd)

        meta = {'email': email,
                'password': password}

        collection = 'user'
        user = yield self.get_collection(collection).find_one(meta)

        if not user:
            self.write("error email or password")
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

    @coroutine
    def post(self):
        username =self.get_argument("username", "")
        email =self.get_argument("email", "")
        passwd =self.get_argument("password", "")
        password = self.encrypt_password(passwd)

        meta = {'username': username,
                'email': email,
                'password': password}

        collection = 'user'
        if(yield self.get_collection(collection).find_one({'username': username})):
            errmessage = "用户名已经存在"

        userid = yield self.put_collection(collection).insert(meta)

        self.redirect('/login')
