#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

class Clase(Calculadora):
  "Esto es un ejemplo de clase que hereda de ClaseMadre"

	def __init__(self, valor):
    "Esto es el método iniciliazador"
    self.atributo = valor
    def __suma__(self,operando1,operando2):
    	return operando1 + operando2

    def __resta__(self,operando1,operando2):
    	return opernado1 - operando2

if __name__ == "__main__":
  objeto = Clase("pepe") # Creo un objeto de la clase Clase
                         # y le paso el valor pepe para su
                         # atributo en la inicialización
