#!/usr/bin/env python3.5
# coding=utf-8

from user.handler import IndexHandler, LoginHandler, LogoutHandler

userurl = (
    (r'/', IndexHandler),
    (r'/login', LoginHandler),
    (r'/logout', LogoutHandler),
)
