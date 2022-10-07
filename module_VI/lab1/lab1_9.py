"""
Program: lab1_9.py
Author: Alejandro Romero

Clases en python y uso de ellas
"""

from functools import reduce


class Student(object):
	""" Representacion de un estudiante """

	def __init__(self, name='', age='', number= 0):
		""" Todo el puntaje se inicia en 0 """
		self._name = name
		self._age = age
		self._scores = []
		for count in range(number):
			self._scores.append(0)

	def getName(self):
		""" Retornando el nombre """
		return self._name
	
	def setName(self, name):
		self._name = name

	def getAge(self):
		""" Retornando la edad """
		return self._age

	def setScore(self, i, score):
		""" Reset del score, countinua desde 1. """
		self._scores[i - 1] = score

	def getScore(self, i):
		""" Retorna el valor del score """
		return self._scores[i - 1]

	def getAverage(self):
		""" Obteniendo el promedio del puntaje """
		summary = reduce(lambda x, y: x + y, self._scores)

		return summary / len(self._scores)

	def __str__(self):
		""" Retornando los string de la clase estudiante """
		return "Nombre: " + self._name + "\nPuntaje : " + " ".join(map(str, self._scores))
