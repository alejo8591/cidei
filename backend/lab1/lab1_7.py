"""
File: lab1_7.py
Para que no se les olvide esto es un comentario del tipo Docstring
"""

bstring = input("Ingrese el string de bits: ")

decimal = 0

exponent = len(bstring) - 1

for digit in bstring:
	decimal = decimal + int(digit) * 2 ** exponent
	exponent = exponent - 1

print("El valor entero es: ", decimal)
