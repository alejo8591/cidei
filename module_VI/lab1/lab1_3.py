#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Program: lab1_3.py
Author: Alejandro Romero

1. Ingresar el valor para saber el rango
	a través de la linea de comandos ingresamos el valor de la calificación
2.  Mostrar el tipo de calificación
	Se muestra en linea de comandos la valoración para el rando de la calificación
"""

number = float(input("Ingrese el número de su calificación: "))

if number > 89:
	letter = 'Eres cool'
elif number > 79:
	letter = 'Eres bueno'
elif number > 69:
	letter = 'Alcanza a pasar'
else:
	letter = 'Un caso perdido'

print("Su calificación esta dentro del rango:", letter)
