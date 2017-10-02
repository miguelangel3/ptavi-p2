#!/usr/bin/python3
# -*- coding: utf-8 -*-

import calcoohija
import sys
import csv

calculadora = calcoohija.CalculadoraHija()

cal = {
    "suma":caculadora.suma,
    "resta":calculadora.resta,
    "multiplica":calculadora.multiplica,
    "divide":calculadora.divide
}

def calcula_linea(calcular):

    resultado = int(calcular[1])
    operacion = cal[calcular[0]]

    for calcula in calcular [2:]:

        resultado = operacion(int(resultado),int(calcula))

    print (resultado)

if __name__ == '__main__':

    with open(sys.argv[1],newline='') as csvfile:
        calcular = csv.reader(csvfile)
        calcula_linea(calcular)
