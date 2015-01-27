class AddressBook(object):
	""" constructor para clases en Python """
	def __init__(self):
		self.data_store = []

	def add_contact(self, contact):
		""" Adicionando un contacto """
		self.data_store.append(contact)

	def all_contacts(self):
		return self.data_store

	def print_contacts(self):
		for contact in self._data_store:
			print(contact)

class Contact(object):
	# Constructor
	def __init__(self, name, email='', phone=''):
		self.name = name
		self.email = email
		self.phone = phone

	def __str__(self):
		return "%s - %s - %s" % (self.name, self.email, self.phone)


class Bussines(Contact):
	# Constructor de la clase Bussiness
	def __init__(self, name='', email='', phone=''):
		self._name = name
		self._email = email
		self._phone = phone
		self._employees = []

	# Metodo adicionar empleado
	def add_employee(self, employee):
		self._employees.append(employee)

	# Metodo para mostrar todos los empleados en lista
	def all_employees(self):
		return self._employees

	# Imprimir todos los resultados de la lista de empleados
	def print_employees(self):
		for e in self._employees:
			print(e)
	# Representa string de una clase, que a su vez un objeto
	def __str__(self):
		return "Tarjeta de negocios para empleado: %s - %s - %s" % (self._name, self._email, self._phone)




