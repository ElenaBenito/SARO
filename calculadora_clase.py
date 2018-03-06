#!/usr/bin/python3

##CORRECCIÓN DEL EJERCICIO CALCULADORA

import sys



def sumar(sumando1, sumando2):
	return sumando1 + sumando2

def restar(sumando1, sumando2):
	return sumando1 - sumando2

def multiplicar(factor1, factor2):
	return factor1 * factor2

def dividir(factor1, factor2):
	try:
		return factor1 / factor2
	except: ZeroDivisionError:
		sys.exit("No se puede dividir entre 0")

funciones = {
	"sumar": sumar
	"restar": restar
	"multiplicar": multiplicar
	"dividir": dividir
}

if __name__ == "__main__":

NUM_ARG = 4

if len(sys.argv) != NUM_ARG:
	sys.exit("Error. Escriba python3 calculadora.py funcion operando1 operando2")

try:
	op1 = float(sys.argv[2])
	op2 = float(sys.argv[3])
except VAlueError:
	print ("No es posible operar con chars")
	sys.exit()

funcion = sys.argv[1]

try:
	resultado = funciones[funcion][op1, op2]
except KeryError:
	sys.exit("Funcion"+ funcion + "no definida")
print (resultado)

