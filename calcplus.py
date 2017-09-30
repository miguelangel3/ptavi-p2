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

def readlines(file_descriptor):

	for line in file_descriptor.readlines():
		#operacion = line[:line.find(",")]
		calcular = line.split(",")

		operación = 



		print (calcular)

if __name__ == '__main__':

	file_descriptor = open("fichero")
	dicionario = {}
	operando = {}

	readlines(file_descriptor)

	#print (operacion)
