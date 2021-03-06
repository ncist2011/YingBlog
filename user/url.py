#!/usr/bin/env python3.5
# coding=utf-8

from user.handler import IndexHandler, LoginHandler, LogoutHandler, RegisterHandler

userurl = (
    (r'/', IndexHandler),
    (r'/login', LoginHandler),
    (r'/logout', LogoutHandler),
    (r'/register', RegisterHandler),
)
