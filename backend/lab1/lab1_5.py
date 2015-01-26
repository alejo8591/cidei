sum = 0.0 
data = input("Ingrese un numero: ")

while data != "":
	number = float(data)
	sum+=number
	data = input("Ingrese el siguiente numero: ")
	number = float(data)
	sum+=number

print "Esa suma extrana es: ", sum
