"""
Program: lab1_10.py
Author: Alejandro Romero

Clases en python y uso de ellas
"""


class X(object):
    def __init__(self):
        self._x = []
        self._y = 0

    def setX(self, x):
        self._x = x

    def __str__(self):
        return self._x


class Z(object):
    def __init__(self):
        self._a = 0
        self._b = 0


class Y(X, Z):
    def __init__(self, x, y):
        self._y = y
        super(Y, self).__init__()

    def __str__(self):
        return "Hola mundo"
