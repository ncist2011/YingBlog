#!/usr/bin/env python3.5
# coding=utf-8

import pymongo

db = pymongo.MongoClient("127.0.0.1", 27017)

class Connection():
    @classmethod
    def get_database(self):
        db = pymongo.Connection(localhost, 27017)
        return db

    @classmethod
    def get_collection(self, collection):
        db = self.get_database()
        coll = db[collection]
        return collection

    @classmethod
    def insert(self, collection, meta):
        coll = self.get_collection(collection)
        coll.insert(meta)

    @classmethod
    def get_document(self, collection, meta):
        coll = self.get_collection(collection)
        document =  coll.find_one(meta)

        if document:
            return True
        else:
            return False
