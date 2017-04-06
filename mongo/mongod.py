#!/usr/bin/env python3.5
# coding=utf-8

import pymongo

db = pymongo.MongoClient("127.0.0.1", 27017)

class Connection():
    @classmethod
    def get_connection(self):
        connection = pymongo.Connection(localhost, 27017)
        return connection

    @classmethod
    def get_database(self):
        connection = self.get_connection()
        db = db['yingblog']
        return db

    @classmethod
    def get_collection(self, collection):
        db = self.get_database()
        coll = db[collection]
        return coll

    @classmethod
    def get_document(self, collection, meta):
        coll = self.get_collection(collection)
        doc = coll.find_one(meta)
        return doc

    @classmethod
    def insert(self, collection, meta):
        coll = self.get_collection(collection)
        coll.insert(meta)

