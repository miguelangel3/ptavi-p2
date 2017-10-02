#!/usr/bin/python3
# -*- coding: utf-8 -*-

import calcoohija
import sys
import csv

calculadora = calcoohija.CalculadoraHija()

cal = {
    "suma": calculadora.suma,
    "resta": calculadora.resta,
    "multiplica": calculadora.multiplica,
    "divide": calculadora.divide
}


def calcula_linea(file_descriptor):

    for line in file_descriptor:

        calcular = line
        resultado = int(calcular[1])
        operacion = cal[calcular[0]]

        for calcula in calcular[2:]:

            resultado = operacion(int(resultado), int(calcula))

        print(resultado)

if __name__ == '__main__':

    with open(sys.argv[1], newline='') as csvfile:
        file_descriptor = csv.reader(csvfile)
        calcula_linea(file_descriptor)
