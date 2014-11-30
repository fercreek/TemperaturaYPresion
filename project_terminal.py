#!/usr/bin/python
# -*- coding: latin-1 -*-
from math import sqrt
from math import pow
from math import pi
from math import log1p
from math import log
from math import e
import csv

print "Transferencia de calor"
print "Producto Integrador"
print "Jorge Luis Barraza Santos 1542818"
print "Lunes, Miercoles, y Viernes M4"

system = input("El sistema es lineal(1) o escalonado(2)? ")
while system not in (1,2):
	system = input("El sistema es lineal(1) o escalonado(2)? ")
	print "Has introduccido una respuesta invalida, por favor ingresa una opcion."

print "Dame los siguientes datos: "
###Variables a introducir
# L  = 3
# TS = 100 
# TI = 20 
# Vmed = 5.2
# D = 0.016
# SL = 0.04
# ST = 0.04
# NFilas = 20
# NTubos = 10

L  = input("Longitud de tubo(L): ___ [m] ")
TS = input("Temperatura de condensacion(TS): ___ [°C] ")
TI = input("Temperatura de entrada: ___ [°C] ")
Vmed = input("Velocidad media(V): ___ [m/s] ")
D = input("Diametro exterior(D): ___ [m] ")
SL = input("SL: ___ [m] ")
ST = input("ST: ___ [m] ")
NFilas = input("Numero de filas de tubos: (NT) ")
NTubos = input("Numero de tubos en cada fila: (NL) ")
Temp = (TS + TI)/2

try:
	with open('table.csv', 'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			if str(Temp) == row[0]:
				print row
				Den = float(row[1])
				Cesp = float(row[2])
				Cterm = float(row[3])
				Dterm = float(row[4])
				Vdin =  float(row[5])
				Vcin = float(row[6])
				Pr = float(row[7])
			if str(TS) == row[0]:
				Prs = float(row[7])
finally: 
	f.close()

# Den = 1.059
# Pr = 0.7202
# Prs = 0.7111
# Temp = 60
# CP = 1007
# Cterm = 0.02808
# Dterm= 2.632e-5
# Vdin = 2.008e-5
# Vcin = 1.896e-5


if system == 1:
	print ST
	print D
	print Vmed
	Vmax = (ST / (ST-D)) * Vmed
	print type(Den)
	print type(Vmax)
	print type(D)
	print type(Vcin)
	ReD = float(Den * Vmax *D)/float(Vcin)
	print ReD
	if ReD <= 100:
		NuD = 0.9 * pow(ReD,0.4)*pow(Pr,0.36)*pow((Pr/Prs),0.25)
	else:
		if ReD <= 1000:
			NuD = 0.52 * pow(ReD,0.5)*pow(Pr,0.36)*pow((Pr/Prs),0.25)
		else:
			if ReD <= 2e5:
				NuD = 0.27 * pow(ReD,0.63)*pow(Pr,0.36)*pow((Pr/Prs),0.25)
			else:
				if ReD <= 2e6:
					NuD = 0.033 * pow(ReD,0.8)*pow(Pr,0.4)*pow((Pr/Prs),0.25)
				else:
					print "El problema no puede ser resuelto de esta manera"

else:
	SD = sqrt( pow(SL,2) + pow((ST/2),2))
	if (2*float(SD - D) < float(ST - D)): #Tengo duda si esto esta bien
		Vmax = (ST / 2(ST-D)) * Vmed
	else:
		Vmax = (ST / (ST-D)) * Vmed
	ReD = float(Den * Vmax *D)/float(Vcin)
	if ReD <= 500:
		NuD = 1.04 * pow(ReD,0.4)*pow(Pr,0.36)*pow((Pr/Prs),0.25)
	else:
		if ReD <= 2e5:
			NuD = 0.35 * pow((ST/ SL),0.2)*pow(ReD,0.6)*pow(Pr,0.36)*pow((Pr/Prs),0.25)
		else:
			if ReD <=2e6:
				NuD = 0.031 * pow((ST/ SL),0.2)*pow(Red,0.8)*pow(pr,0.36)*pow((pr/prs),0.25)
			else:
				print "El problema no puede ser resuelto de esta manera"

HB = (NuD*Cterm)/D
N  = NFilas * NTubos
As = N * pi * D * L
M  = Den * Vmed * ST * L * NTubos
TE = TS - (TS - TI ) * pow(e,(((-1)*As*HB)/(M*Cesp))) #De donde saco CP???
A = (TS - TE) - (TS -TI)
B = log((TS-TE)/(TS-TI))
Tim = (A/B)
Q = HB * As * Tim
print "a)"
print "Q: ", Q , " w/m^2 * °C"
print "HB: ", HB, " w"

FX = input("Dame el FX de la tabla 7-27: ")
PX = float(NFilas * FX) * ((Den*pow(Vmax,2))/(2))
print "b)"
print "PX", PX, " Pa"