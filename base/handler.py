#!/usr/bin/env python3.5
# encoding: utf-8

import tornado.web
from tornado.gen import coroutine

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        user_id = self.get_secure_cookie("userid")
        if user_id is None:
            return None
        else:
            return user_id

    def get_database(self):
        connection = self.settings['connection']
        db = connection['yingblog']
        return db

    def get_collection(self, collection):
        db = self.get_database()
        coll = db[collection]
        return coll
