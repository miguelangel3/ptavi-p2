#!/usr/bin/python3
# -*- coding:utf-8 -*-

import sys
import calc


class Calculadora:
    def __init__(self):
        self.operations = {"suma": self.sum, "resta": self.substraction}

    def operating(self, calculator_operation, op1, op2):
        return calculator_operation(op1, op2)

    def sum(self, a, b):
        return a + b

    def substraction(self, a, b):
        return a - b



def do_operation(calculator, operation, op1, op2):

    try:
        return calculator.operating(calculator.operations[operation],
                                    op1, op2)
    except KeyError:
        sys.exit("Not allowed operation " + operation)

if __name__ == "__main__":
    op1 = calc.to_number(sys.argv[1])
    operation = sys.argv[2]
    op2 = calc.to_number(sys.argv[3])
    calculator = Calculadora()
    print(do_operation(calculator, operation, op1, op2))