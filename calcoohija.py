#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo

class CalculadoraHija(calcoo.Calculadora):
	def __init__(self, arg):
		pass

	def multiplica(self,operando1,operando2):
		return operando1 * operando2

	def divide(self,operando1,operando2):
		try 
			return operando1 / operando2
		except ZeroDivisionError
			sys.exit("No se puede dividir entre 0") 

if __name__ == '__main__':
	try:
		operando1 = int(sys.argv[1])
		operando2 = int(sys.argv[3])

	except ValueError:
		sys.exit("Los operandos tienen que ser enteros")

	if operador == "suma":
		resultado = CalculadoraHija().suma(operando1,operando2)
	elif operador == "resta":
		resultado = CalculadoraHija().resta(operando1,operando2)
	elif operador == "multiplica":
		resultado = CalculadoraHija().multiplica(operando1,operando2)
	elif operador == "divide":
		resultado = CalculadoraHija().divide(operando1,operando2)
	else:
		sys.exit("El operador solo puede ser sumar,restar,multiplicar o dividir")

	print ("El resultado de " + sys.argv +"es: ", (resultado))