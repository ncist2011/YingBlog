#!/usr/bin/env python3.5
# coding=utf-8

import pymongo

db = pymongo.MongoClient("127.0.0.1", 27017)

class Connection():
    @classmethod
    def get_connection(self):
        db = pymongo.Connection(localhost, 27017)
        return db

    @classmethod
    def get_database(self):
        connection = self.get_connection()
        db = db['yingblog']
        return db

    @classmethod
    def get_document(self, collection, meta):
        coll = self.get_collection()
	doc = coll[collection]
        document = doc.find_one(meta)

        if document:
            return True
        else:
            return False

    @classmethod
    def insert(self, collection, meta):
        coll = self.get_collection()
	doc = coll[connection]
        doc.insert(meta)

