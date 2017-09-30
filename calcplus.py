#!/usr/bin/python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

	file_descriptor = open("fichero")
	dicionario = {}

	for line in file_descriptor.readlines():
		operacion = line[:line.find(",")]

		print (operacion)
