sum = 0.0 
data = raw_input("Ingrese un numero: ")

while data != "":
	number = float(data)
	sum+=number
	data = raw_input("Ingrese el siguiente numero: ")
	number = float(data)
	sum+=number

print "Esa suma extrana es: ", sum