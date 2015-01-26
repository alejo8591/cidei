# -*- coding: utf-8 -*-
"""
File: lab1_8.py
Convertir de decimal a binario
"""

decimal = input("Ingrese el número decimal a Convertir: ")

if decimal == 0:
	print(0)
else:
	print("Resto del cociente binario")
	bstring = ""
	while decimal > 0:
		remainder = decimal % 2
		decimal = decimal / 2
		bstring = str(remainder) + bstring
		print "%5d%8d%12s" % (decimal, remainder, bstring)
	print("La representación binaria es: ", bstring)
