#!/usr/bin/python3
# -*- coding: utf-8 -*-

import calcoo
import calcoohija

cal = [calcoo,calcoohija]

def operando (line,operacionfind):
	#for string in line:
	pass
def operacion (line):

	return line[:line.find(",")]
	#return operacion = line[:line.find(",")] 

def tostring (line):
	pass

def calculalinea (file_descriptor):

	for line in file_descriptor.readlines():
		
		calcular = line.split(",")

		operacion = calcular[0]

		print (operacion)

if __name__ == '__main__':

	file_descriptor = open("fichero")
	dicionario = {}
	operando = {}

	calculalinea(file_descriptor)

	#print (operacion)
