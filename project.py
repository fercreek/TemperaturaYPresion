###Variables a introducir
# L  = raw_input("Longitud de tubo: ")
# TS = raw_input("Temperatura de condensacion: ")
# TI = raw_input("Temperatura de entrada: ")
# V = raw_input("Velocidad media: ")
# D = raw_input("Diametro exterior: ")
# SL = raw_input("SL: ")
# ST = raw_input("ST: ")
# NFilas = raw_input("Numero de filas de tubos: ")
# NTubos = raw_input("Numero de tubos en cada fila: ")

###Variables del sistema
Vmax
ReD
NuD
HB
As
M 
TE 
Tim
Q
SD
px
PT 
N 
H 
C 
gv
TEM 

system = input("El sistema es escalonado(1) o lineal(2)? ")
while system not in (1,2):
	system = input("El sistema es escalonado(1) o lineal(2)? ")
	print "Has introduccido una respuesta invalida, por favor ingresa una opcion."
