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


def calcula_linea (file_descriptor):

	for line in file_descriptor.readlines():

		calcular = line.split(",")
		resultado = int(calcular[1])
		operacion = cal[calcular[0]]

		for calcula in calcular [2:]:

			resultado = operacion(int(resultado),int(calcula))

		print (resultado)

if __name__ == '__main__':

	file_descriptor = open("fichero")
	calcula_linea(file_descriptor)
