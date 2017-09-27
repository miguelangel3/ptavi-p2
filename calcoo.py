#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

class Calculadora():


    def suma(self,operando1,operando2):
    	return operando1 + operando2

    def resta(self,operando1,operando2):
    	return operando1 - operando2

if __name__ == "__main__":

	try:
		operando1 = int(sys.argv[1])
		operando2 = int(sys.argv[3])
	except ValueError:
		sys.exit("Error: Non numerical parameters")

	if sys.argv[2] == "suma":
		result = Calculadora.suma(operando1, operando2)
	elif sys.argv[2] == "resta":
		result = Calculadora.resta(operando1, operando2)
	else:
		sys.exit('Operación sólo puede ser sumar o restar.')

	print(result)
