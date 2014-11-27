from math import sqrt
from math import pow
from math import pi
from math import log1p
from math import log
from math import e

# Variables Declaradas #####
L = 3
TS = Tcondensacion = 100
TI = Tentrada = 20
Ventrada = 5.2
D = 0.016 #diametro exterior
ST = SL = 0.04 #m
NL = 20 #filas
NT = 10 #tubos
Temp = (Tentrada + Tcondensacion)/2
Ve = 5.2
Den = Densidad = 1.059 #kg/m^3
CP =1007 #calor especifico
cond_termica = 0.02808
difusividad_termica = 2.632e-5
viscosidad_dinamica = 2.008e-5
viscosidad_cinematica = 1.896e-5
pr = 0.7202
prs = 0.7111 #se obtiene de la temp de condensacion
	
SD = sqrt( pow(SL,2) + pow((ST/2),2))
print "SD: ", SD

if SD < (ST + D)/2:
	print "if" 
	Vmax = (ST / 2(ST-D)) * Ve
else:
	print "else"
	Vmax = (ST / (ST-D)) * Ve #lineal

print "Vmax original: ", Vmax
Vmax = "{0:.2f}".format(Vmax)
Vmax = float(Vmax)

#### Solo aplica en este caso por el momento ya que sale 8.67.
Vmax = 8.66 

Red = float(Den * Vmax *D)/float(viscosidad_dinamica)
print "Red ", Red

NuD = 0.35 * pow((ST/ SL),2)*pow(Red,0.6)*pow(pr,0.36)*pow((pr/prs),0.25)
NuD = "{0:.2f}".format(NuD)
NuD = float(NuD)

print "NuD: ",NuD

print "cond ", cond_termica
print "D ", D
h = (NuD*cond_termica)/D
h = "{0:.2f}".format(h)
h = float(h)

print "h: ", h

N=NL*NT
As = N * pi * D * L
m = Den * Ventrada * NT * ST * L
m = "{0:.2f}".format(m)
m = float(m)

print "m: ", m

#####se va a sobreescribir h mientras se aclara la duda

h= 75.16

Te = TS - (TS - TI ) * pow(e,(((-1)*As*h)/(m*CP)))
# print TS, TI, As, h, m, CP

print "Te: ", Te

A = (TS - Te) - (TS -TI)
B = log((TS-Te)/(TS-TI))
Tim = (A/B)
print "A",A 
print "B",B
print "Tim", Tim

###### Aca h otra vez se vuelve 113.93
h = 113.93


Q = h * As * Tim
print "Q: ",Q
print "h: ", h
print "b) Caida de presion"
fx = 2.5
print N, fx, Den, Vmax
DifP = NL * fx * ((Den*pow(Vmax,2))/(2))
print "Dif P: ", DifP