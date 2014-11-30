#!/usr/bin/python
# -*- coding: latin-1 -*-

from Tkinter import *
from math import sqrt
from math import pow
from math import pi
from math import log1p
from math import log
from math import e
import csv

def sel():
	selection = str(option.get())
	return int(selection)

def start():
	operations(L.get(), TS.get(),TI.get(),
			Vmed.get(),D.get(),SL.get(),
			ST.get(),NFilas.get(),NTubos.get(),
			FX.get())

def operations(L,TS,TI,Vmed,D,SL,ST,NFilas,NTubos,FX):
	L = float(L)
	TS = float(TS)
	TI = float(TI)
	Vmed=float(Vmed)
	D = float(D)
	SL = float(SL)
	ST = float(ST)
	NFilas = float(NFilas)
	NTubos = float(NTubos)
	FX = float(FX) 
	Temp = (TS + TI)/2
	# print TS
	# print TI
	# print Temp
	try:

		with open('table.csv', 'rb') as f:
			reader = csv.reader(f)
			for row in reader:
				if str(int(Temp)) == row[0]:
					# print row
					Den = float(row[1])
					Cesp = float(row[2])
					Cterm = float(row[3])
					Dterm = float(row[4])
					Vdin =  float(row[5])
					Vcin = float(row[6])
					Pr = float(row[7])
				if str(int(TS)) == row[0]:
					Prs = float(row[7])
	finally: 
		f.close()


	system = sel()
	# system = 1
	if system == 1:
		Vmax = (ST / (ST-D)) * Vmed
		ReD = (Den * Vmax *D)/(Vcin)
		
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
						print "chale"
						Error=Label(master,text="Este problema no puede ser resuelto ", font=("Agency FB", 10)).place(x=300,y=140)
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
					Error=Label(master,text="Este problema no puede ser resuelto ", font=("Agency FB", 10)).place(x=340,y=400)

	HB = (NuD*Cterm)/D
	N  = NFilas * NTubos
	As = N * pi * D * L
	M  = Den * Vmed * ST * L * NTubos
	TE = TS - (TS - TI ) * pow(e,(((-1)*As*HB)/(M*Cesp))) #De donde saco CP???
	A=(TS - TE) - (TS -TI)
	B=log((TS-TE)/(TS-TI))
	Tim = (A/B)
	Q = HB * As * Tim
	PX = (float(NFilas) * float(FX)) * ((Den*pow(Vmax,2))/(2))
	showResults(Q,HB,PX)

def showResults(Q, HB, PX):
	a=Label(master,text="a) " + "Q: " + str(float(Q)) +  "w/m^2 * °C", 
		font=("Agency FB", 10)).place(x=10,y=400)
	b=Label(master,text="HB:  " + str(float(HB)) +  " w",
		font=("Agency FB", 10)).place(x=10,y=420) 
	c=Label(master,text="b) " + "PX  " + str(float(PX)) +  " Pa", font=("Agency FB", 10)).place(x=10,y=440)

master = Tk()
master.geometry("700x500+100+100")
master.title("Presiones")
Encabezado=Label(text="Transferencia de calor - Producto Integrador", font=("Agency FB", 14)).place(x=10,y=10)
Datos=Label(text="Jorge Luis Barraza Santos 1542818 - Lunes, Miercoles, y Viernes M4", font=("Agency FB", 10)).place(x=10,y=40)

option = IntVar()
system=Label(text="Tipo de sistema.", font=("Agency FB", 12)).place(x=10,y=70)
lineal=Label(text="Lineal.", font=("Agency FB", 10)).place(x=20,y=90)
escalonado=Label(text="Escalonado.", font=("Agency FB", 10)).place(x=20,y=110)
R1 = Radiobutton(master, variable=option, command= sel ,value=1).place(x=100,y=90)
R2 = Radiobutton(master, variable=option, command= sel, value=2).place(x=100,y=110)

L_txt=Label(text="Longitud de tubo(L): ", font=("Agency FB", 10)).place(x=20,y=140)
TS_txt=Label(text="Temperatura de condensacion(TS):  ", font=("Agency FB", 10)).place(x=20,y=160) 
TI_txt=Label(text="Temperatura de entrada:  ", font=("Agency FB", 10)).place(x=20,y=180) 
Vmed_txt=Label(text="Velocidad media(V):  ", font=("Agency FB", 10)).place(x=20,y=200) 
D_txt=Label(text="Diametro exterior(D): ", font=("Agency FB", 10)).place(x=20,y=220) 
SL_txt=Label(text="SL: ", font=("Agency FB", 10)).place(x=20,y=240) 
ST_txt=Label(text="ST: ", font=("Agency FB", 10)).place(x=20,y=260) 
NFilas_txt=Label(text="Numero de filas de tubos: (NT) ", font=("Agency FB", 10)).place(x=20,y=280) 
NTubos_txt=Label(text="Numero de tubos en cada fila: (NL) ", font=("Agency FB", 10)).place(x=20,y=300) 
FX=Label(text="FX de la tabla 7-27: ", font=("Agency FB", 10)).place(x=20,y=320) 

L_txt=Label(text="m ", font=("Agency FB", 10)).place(x=340,y=140)
TS_txt=Label(text="°C ", font=("Agency FB", 10)).place(x=340,y=160) 
TI_txt=Label(text="°C ", font=("Agency FB", 10)).place(x=340,y=180) 
Vmed_txt=Label(text="m/s ", font=("Agency FB", 10)).place(x=340,y=200) 
D_txt=Label(text="m ", font=("Agency FB", 10)).place(x=340,y=220) 
SL_txt=Label(text="m ", font=("Agency FB", 10)).place(x=340,y=240) 
ST_txt=Label(text="m ", font=("Agency FB", 10)).place(x=340,y=260) 

L = StringVar()
L.set(0.0)
txtUsuario = Entry(master,textvariable=L, width=10).place(x=250,y=140)
TS = StringVar()
TS.set(0.0)
txtUsuario = Entry(master,textvariable=TS, width=10).place(x=250,y=160)
TI = StringVar()
TI.set(0.0)
txtUsuario = Entry(master,textvariable=TI, width=10).place(x=250,y=180)
Vmed = StringVar()
Vmed.set(0.0)
txtUsuario = Entry(master,textvariable=Vmed, width=10).place(x=250,y=200)
D = StringVar()
D.set(0.0)
txtUsuario = Entry(master,textvariable=D, width=10).place(x=250,y=220)
SL = StringVar()
SL.set(0.0)
txtUsuario = Entry(master,textvariable=SL, width=10).place(x=250,y=240)
ST = StringVar()
ST.set(0.0)
txtUsuario = Entry(master,textvariable=ST, width=10).place(x=250,y=260)
NFilas = StringVar()
NFilas.set(0.0)
txtUsuario = Entry(master,textvariable=NFilas, width=10).place(x=250,y=280)
NTubos = StringVar()
NTubos.set(0.0)
txtUsuario = Entry(master,textvariable=NTubos, width=10).place(x=250,y=300)
FX = StringVar()
FX.set(0.0)
txtUsuario = Entry(master,textvariable=FX, width=10).place(x=250,y=320)

# btn = Button(master, text="Enter", 
# 			command=operations(L.get(), TS.get(),TI.get(),
# 								Vmed.get(),D.get(),SL.get(),
# 								ST.get(),NFilas.get(),NTubos.get(),
# 								FX.get()),
# 			font=("Agency FB", 12),
# 			width=10).place(x=250,y=350)

btn = Button(master, text="Enter", 
			command=start,
			font=("Agency FB", 12),
			width=10).place(x=250,y=350)

master.mainloop()