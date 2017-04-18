#!/usr/bin/env python3.5
# encoding: utf-8

import hashlib
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
        db = self.settings['db']
        return db

    def get_collection(self, collection):
        db = self.get_database()
        coll = db[collection]
        return coll

    def encrypt_password(self, password):
        passwd = hashlib.md5(password).hexdigest()
        return passwd

    @coroutine
    def put_collection(self, collection):
        db = self.get_database()
        dbs = yield db.collection_names()

        if collection not in dbs:
            yield db.create_collection(collection)

        col = self.get_collection(collection)
        return col
