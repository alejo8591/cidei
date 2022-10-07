"""
Program: lab1_11.py
Author: Alejandro Romero

Clases en python y uso de ellas
"""


class A(object):
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def __str__(self):
        return "%s - %s - %s" % (self._x, self._y, self._z)


class B(A):
    def __init__(self, x, y, z, c, d):
        self._c = c
        self._d = d
        A.__init__(self, x, y, z)

    def __str__(self):
        return "%s - %s - %s" % (self._x, self._y, self._z)
