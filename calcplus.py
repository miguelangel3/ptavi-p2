#!/usr/bin/python3
# -*- coding: utf-8 -*-


import calcoohija
import sys

calculadora = calcoohija.CalculadoraHija()

cal = {
    "suma": calculadora.suma,
    "resta": calculadora.resta,
    "multiplica": calculadora.multiplica,
    "divide": calculadora.divide
}


def calcula_linea(file_descriptor):

    for line in file_descriptor.readlines():

        calcular = line.split(",")
        resultado = int(calcular[1])
        operacion = cal[calcular[0]]

        for calcula in calcular[2:]:
            try:
                resultado = operacion(int(resultado), int(calcula))
            except ValueError:
                sys.exit("Error: Non numerical parameters")
        print(resultado)

if __name__ == '__main__':

    file_descriptor = open(sys.argv[1])
    calcula_linea(file_descriptor)
    file_descriptor.close()
