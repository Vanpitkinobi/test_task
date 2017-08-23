#!/usr/bin/env python


class MyError(Exception):
    pass


class Parent(object):
    pass


class First(Parent):
    pass


class Second(Parent):
    pass


class A(First):
    def __init__(self):
        self.i = 3
        self.isSecond = False

    def __setattr__(self, key, value):
        if key == 'isSecond' and not isinstance(value, bool):
            raise AttributeError('wrong isSecond attribute type')
        self.__dict__[key] = value

    def fnc(self, n):
        if n == 7:
            raise MyError('Error text')
        return n*n*3

    def isFirst(self):
        return True

    def isSecond(self):
        return False


