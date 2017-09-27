#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

class Clase(Calculadora):
  "Esto es un ejemplo de clase que hereda de ClaseMadre"

	def __init__(self, valor):
    "Esto es el método iniciliazador"
    self.atributo = valor
    def suma (self,operando1,operando2):
    	return operando1 + operando2

    def resta (self,operando1,operando2):
    	return operando1 - operando2

if __name__ == "__main__":
  
	try:
    	operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        result = suma(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = resta(operando1, operando2)
    else:
        sys.exit('Operación sólo puede ser sumar o restar.')

    print(result)
