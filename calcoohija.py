#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo


class CalculadoraHija(calcoo.Calculadora):

    def multiplica(self, operando1, operando2):
        return operando1 * operando2

    def divide(self, operando1, operando2):
        try:
            return operando1 / operando2
        except ZeroDivisionError:
            sys.exit("Division by zero is not allowed")

if __name__ == '__main__':

    try:
        operando1 = int(float(sys.argv[1]))
        operando2 = int(float(sys.argv[3]))
    except ValueError:
        sys.exit("Error: Non numerical parameters")
    operador = sys.argv[2]

    if operador == "suma":
        resultado = CalculadoraHija().suma(operando1, operando2)
    elif operador == "resta":
        resultado = CalculadoraHija().resta(operando1, operando2)
    elif operador == "multiplica":
        resultado = CalculadoraHija().multiplica(operando1, operando2)
    elif operador == "divide":
        resultado = CalculadoraHija().divide(operando1, operando2)
    else:
        sys.exit("El operador no es válido")

    print("El resultado de " + sys.argv[2] + " es:", (resultado))
