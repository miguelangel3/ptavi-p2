#!/usr/bin/python3
# -*- coding: utf-8 -*-

import calcoohija
import sys
import csv
from calcplus import cal

calculadora = calcoohija.CalculadoraHija()


def calcula_linea(file_descriptor):

    for line in file_descriptor:

        calcular = line
        resultado = int(calcular[1])
        operacion = cal[calcular[0]]

        for calcula in calcular[2:]:
            try:
                resultado = operacion(int(resultado), int(calcula))
            except ValueError:
                sys.exit("Error: Non numerical parameters")
        print(resultado)

if __name__ == '__main__':

    with open(sys.argv[1], newline='') as csvfile:
        file_descriptor = csv.reader(csvfile)
        calcula_linea(file_descriptor)
