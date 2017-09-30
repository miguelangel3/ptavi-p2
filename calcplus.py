#!/usr/bin/python3
# -*- coding: utf-8 -*-


import calcoohija

calculadora = calcoohija.CalculadoraHija()

cal = {
	"suma":calculadora.suma,
	"resta":calculadora.resta,
	"multiplica":calculadora.multiplica,
	"divide":calculadora.divide
}


def operando (line,operacionfind):
	#for string in line:
	pass

def resta (val1,val2):
	pass

def divide(val1,val2):
	pass

def multiplica (val1,val2):
	pass

#def suma (val1,val2):

#	return val1 + val2
	
def tostring (line):
	pass

def calcula_linea (file_descriptor):

	for line in file_descriptor.readlines():

		calcular = line.split(",")
		resultado = int(calcular[1])
		calcular = line.split(",")
		operacion = cal[calcular[0]]

		for calcula in calcular [2:]:

			resultado = operacion(int(resultado),int(calcula))

		print (resultado)

if __name__ == '__main__':

	file_descriptor = open("fichero")
	dicionario = {}
	operando = {}

	calcula_linea(file_descriptor)

	#print (operacion)
