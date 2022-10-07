# -*- coding: utf-8 -*-
"""
Program: lab1_6.py
Author: Alejandro Romero

Generador de sentencias aleatorio con palabras
"""

import random

articles = ("Un", "El", "Ella", "Nosotros", "Yo",)

nouns = ("Mujer", "Hombre", "Carro", "Moto", "Perro", "Avion",)

verbs = ("Gustar", "Hablar", "Comer", "Decir",)

prepositions = ("con", "por",)


def sentences():
    """ Construir y retornar una oración o sentencia """
    return "%s %s" % (nounPhrase(), verbPhrase())


def nounPhrase():
    """ Construir y retornar una frase con palabras """
    return "%s %s" % (random.choice(articles), random.choice(nouns))


def verbPhrase():
    """ Construir y retornar una frase con verbo """
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()


def prepositionalPhrase():
    """ Construir y retornar una preposition a la frase """
    return random.choice(prepositions) + " " + nounPhrase()


def main():
    """ El usuario genera el número de frases a construir """
    number = int(input("Ingrese el numero de frases a Construir: "))
    for count in range(number):
        print(sentences())


main()
