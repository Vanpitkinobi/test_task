#!/usr/bin/env python
from ma import Second


class B(Second):
    def __init__(self, first_value):
        self.first_value = first_value
        self.isSecond = True

    def fnc(self, n, m):
        return n*m*5

    def isFirst(self):
        return False

