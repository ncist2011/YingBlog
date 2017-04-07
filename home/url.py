#!/usr/bin/env python3.5
# encoding: utf-8

from home.handler import HomeBaseHandler, HomeEntry

homeurl = (
    (r'/homebase', HomeBaseHandler),
    (r'/homeentry', HomeEntry),
)
