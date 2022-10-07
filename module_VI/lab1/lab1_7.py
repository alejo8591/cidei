"""
Program: lab1_7.py
Author: Alejandro Romero

Clases en python y uso de ellas
"""
class AddressBook(object):
    """ Constructor para clases en Python """

    def __init__(self):
        self._data_store = []

    def add_contact(self, contact):
        """ Adicionando un contacto """
        self._data_store.append(contact)

    def all_contacts(self):
        return self._data_store

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
