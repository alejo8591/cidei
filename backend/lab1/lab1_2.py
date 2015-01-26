#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Program: lab1_2.py
Author: Alejandro Romero

1. Ingresar el valor para saber el rango
	a través de la linea de comandos ingresamos el valor de la calificación
2.  Mostrar el tipo de calificación
	Se muestra en linea de comandos la valoración para el rando de la calificación
"""

number  = int(input("Ingrese el número de su calificación: "))

if number > 89 :
	letter = 'S'
elif number > 79:
	letter = 'B'
elif number > 69:
	letter = 'A'
else:
	letter = 'Un caso perdido'

print("Su calificación esta dentro del rango: ", letter)
