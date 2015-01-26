# Importante modulo completo "random" en python
import random

smaller = int(input("Ingrese el número pequeno: "))
large =  int(input("Ingrese el número grande o mayor: ")) 

my_random_number = random.randint(smaller, large)

print("My número aleatorio es: ", my_random_number)

count = 0

while True:
	count+=1
	user_number = int(input("Ingrese un número para comparar: "))
	if user_number < my_random_number:
		print("Es un número pequeno")
	elif user_number > my_random_number:
		print("Es un número grande")
	else:
		print("Lo tienes en ", count, "Vuelve a intentarlo!")
		break


