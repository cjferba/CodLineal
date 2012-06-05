from numpy import *
import random

# -*- coding: cp1252 -*-

#
#       CODLIN.py
#       
#       Copyright 2012 Carlos Jesus Fernandez Basso <cjferba@gmail.com>
#       
STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE= -11
STD_ERROR_HANDLE = -12

FOREGROUND_BLUE = 0x01 # text color contains blue.
FOREGROUND_GREEN= 0x02 # text color contains green.
FOREGROUND_RED  = 0x04 # text color contains red.
FOREGROUND_VIO  = 0x05
FOREGROUND_AMA  = 0x06
FOREGROUND_INTENSITY = 0x08 # text color is intensified.
BACKGROUND_BLUE = 0x10 # background color contains blue.
BACKGROUND_GREEN= 0x20 # background color contains green.
BACKGROUND_RED  = 0x40 # background color contains red.
BACKGROUND_INTENSITY = 0x80 # background color is intensified.

import ctypes
import random

std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
color= (FOREGROUND_GREEN,FOREGROUND_BLUE,FOREGROUND_RED,FOREGROUND_VIO,FOREGROUND_AMA)
def set_color(color, handle=std_out_handle):
    """(color) -> BOOL
    
    Example: set_color(FOREGROUND_GREEN | FOREGROUND_INTENSITY)
    """
    bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return bool


def std(matriz,zeta):
	n_filas=len(matriz)
	n_columnas=len(matriz[0])
	if n_filas >= n_columnas:
		print "No es posible calcular la Matriz Generadora Estandar ni la Matriz de control cuando k>=n ."
		raise SystemExit
	
	# Intentamos obtener la identidad en el lado izquierdo [I|A]
	flag = False
	for i in range(n_filas):
		for j in range(n_columnas):
			flag = False
			# Si no puede ser pivote
			# PASO 1
			if i == j and matriz[i][j] == 0:
				# Buscamos un G(i,i) != 0
				for k in range(i,n_filas):
					# Si lo encontramos por filas
					if matriz[k][j] != 0:
						# Intercambiamos las filas
						aux = list(matriz[i])
						matriz[i] = matriz[k]
						matriz[k] = aux
						flag = True
				if not flag:
					# Si no lo hemos encontrado por filas
					for h in range(n_columnas):
						# y lo encontramos por columnas
						if matriz[i][h] != 0:
							# Intercambiamos las columnas
							for z in range(n_filas):
								aux = matriz[z][h]
								matriz[z][h] = matriz[z][j]
								matriz[z][j] = aux
							flag = True
			# Ya es un pivote
			elif i == j and matriz[i][j] != 0:
				flag = True
			# Si no hemos encontrado ningun candidato a pivote
			if i==j and not flag:
				print "Error, no se ha encontrado G(",int(i),",",int(j),") != 0."
				raise SystemExit
			# Si lo hemos encontrado
			elif i==j:
				# PASO 2
				# Colocamos un 1 en G(j,j)
				inv = inverso(matriz[i][j],zeta)
				for s_j in range(n_columnas):
					matriz[i][s_j] = (inv*matriz[i][s_j]) % zeta
				# PASO 3
				# Obtenemos 0 en toda la columna.
				fil = matriz[i]
				for s_i in range(n_filas):
					if s_i != i and matriz[s_i][j] != 0:
						# Obtenemos el inverso para la suma
						sub = zeta - matriz[s_i][j]
						for z in range(n_columnas):
							matriz[s_i][z] = (matriz[s_i][z]+sub*matriz[i][z])%zeta
	return matriz
def inverso(num,zeta):
	
	if zeta == 2:
		return 1
	elif zeta == 3:
		if num == 1:
			return 1
		elif num == 2:
			return 2
	elif zeta == 5:
		if num == 1:
			return 1
		elif num == 2:
			return 3
		elif num == 3:
			return 2
		elif num == 4:
			return 4
"""
Funcion nor(x1)
Funcion que normaliza una matriz mediante 
el Algoritmo de normalizacion de matrices
"""
def nor(x1,z):
	x=x1[:]
	aux=0
	aux1=[]
	f=len(x)
	c=len(x[0])
	for i in range(f):
		if x[i][i]==0:
			cam=buscar(x,i)
			print"OK,busca",cam#por implementar aun
			imprimir(x)
			if isinstance(cam,list):
				aux=x[i][:]
				x[i]=x[cam[0]][:]
				x[cam[0]]=aux
				print 'dentro'
				imprimir(x)
			else:
				 #sys.exit("error,no se puede encontrar cambio de fila/columna")
				 print"error,no se puede encontrar cambio de fila/columna"
				 exit()
		#elif x[i][i]==1:
			#print "bien"
		if x[i][i]<>1:
			aux=x[i][i]#para que las referencias no den problemas
			for s in range(c):
				#print 'pos['+str(i)+']['+str(s)+']:'+str(x[i][s])+'*(1/'+str(x[i][i])+')'
				x[i][s]=x[i][s]/aux
		#Poner 0 en toda la columna donde nos encontramos
		for s in range(f):
			if s<>i:
				if x[s][i]<>0:
					for d in range(c):
						#print 'pos['+str(s)+']['+str(d)+']:'+str(x[s][d])+'-'+str(x[i][d])+'*'+str(x[s][d])
						if x[s][d]==0:
							a=x[i][d]
							x[s][d]=x[s][d]-a
						else:
							a=x[i][d]*x[s][d]
							x[s][d]=x[s][d]-a
	pasarZ(x,z)
	return x[:]
#		for ww in range(f):
#			print x[ww]
#		print '\n'

def pasarZ(x,z):
	if isinstance ( x[0] , list ):
		f=len(x)
		c=len(x[0])
		for s in range(f):
			for d in range(c):
				if x[s][d]<0:
					x[s][d]=x[s][d]+z
				elif x[s][d]>=z:
					x[s][d]=x[s][d]%z
	else:
		f=len(x)
		for s in range(f):
			if x[s]<0:
				x[s]=x[s]+z
			elif x[s]>=z:
				x[s]=x[s]%z

def buscar(x,i):
#busca en matriz X desde la posicion m[i][i] un valor inferior para cambiarlo sino busca por columnas(aun por columnas no realizado)
	c=len(x)-(i+1)
	for s in range(c):
			if x[s+i][i]<>0:
				return [s+i]

def pasoGaCH (G):
	f=len(G)
	c=len(G[0])
	s=c-f
	aux=[]
	aux2=[]
	for i in range(f):
		for x in range(s):
			#print 'aqui:',-G[i][x+f]
			aux.append(-G[i][x+f])
		aux2.append(aux[:])
		aux=[]
	aux3=[]
	for i in range(len(aux2[0])):
		for x in range(len(aux2)):
			aux.append(aux2[x][i])
		aux3.append(aux[:])
		aux=[]
		s=c-f
	for i in range(s):
		for x in range(s):
			if x==i:
				#print 'metemos:',1
				aux3[i].append(1)
			else:
				#print 'metemos:',0
				aux3[i].append(0)
	return aux3[:]

def traspuesta(X):
	f=len(X)
	c=len(X[0])
	aux=[]
	aux2=[]
	for i in range(c):
		for x in range(f):
			aux.append(X[x][i])
		aux2.append(aux[:])
		aux=[]
	return aux2

"""
Funcion imprimir, nos muestra por pantalla
una matrix x pasada como argumento
"""
def imprimir(x):
	if isinstance ( x[0] , list ):
		for i in range(len(x)):
			for s in range(len(x[i])):
				print repr(x[i][s]).rjust(4)+',',
			print '\n'
	else:
			print 'El vector es:',x

########MAIN############
letras=['a','c','d','e','i','p','r','s','t']
#letras=['acdeiprst']
palabras=[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
G=[]#matrix[Filas][Columnas]
Gs=[]
H=[]
Ht=[]
topes=[[0,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0],[0,0,0,2],[0,0,2,0],[0,2,0,0],[2,0,0,0]]
sindrome=[]
iden=[]
iden1=[]
decodificacion=[]
codificacion=[]
codificacion1=[]
m1=[]
#Z en el que trabajaremos
#z=int(raw_input("trabajaremos en Z: "))
z=3
#% de error 
alfa=int(raw_input("Introducir Alfa:\n"))
while (alfa>0) and (alfa>=100):
    alfa=int(raw_input("Introducir Alfa:\n"))
#filas y columnas de la matriz En nuestro caso 2x4
n=2
m=4
#n=int(raw_input("matriz filas:"))
#m=int(raw_input("matriz columnas:"))
for i in range(n):
	for x in range(m):
		entrada=int(raw_input("elemento["+str(i)+"]["+str(x)+"]:"))
		if(x==i):
			m1.append(entrada)
		else:
			m1.append(entrada)
	G.append(m1[:])
	m1=[]


print "Matriz G"
imprimir(G)

print "\nSolucion Estandar "
Gs=std(G,z)
imprimir(Gs)

for i in range(len(palabras)):
	iden.append(dot(palabras[i], Gs))
	iden[i]=iden[i].tolist ()
	pasarZ(iden[i],z)
palabras1=[]
palabras1=iden[:]
#print iden
"""
for i in range(len(iden)):
	print 'Codificacion:',iden[i]
	print 'mala codificacion',iden1[i]"""
H=pasoGaCH(Gs)
pasarZ(H,3)
Ht=traspuesta(H)
m1=[]
print 'H es :'
imprimir(H)
for i in range(len(topes)):
	m1=dot(topes[i],Ht)
	m1=m1.tolist()
	pasarZ(m1,z)
	sindrome.append(m1[:])
	m1=[]
#print 'topes'
#imprimir(topes)
print 'sindromes'
imprimir(sindrome)
cadena=raw_input('Cadena a codi/decodificar[A,C,D,E,I,P,R,S,T]')
for i in range(len(cadena)):
	a=letras.index(cadena[i])
	m1=dot(palabras[a],Gs)
	m1=m1.tolist()
	pasarZ(m1,z)
	codificacion.append(m1[:])
	m1=[]
print 'codificacion',codificacion
for i in range(len(codificacion)):
	for u in range(len(codificacion[i])):
		a=random.randint(1,100)
		if a<=alfa:
			if codificacion[i][u]==0:
				m1.append(1)
			else:
				m1.append(0)
		else:
			m1.append(codificacion[i][u])
	codificacion1.append(m1[:])
	m1=[]

print "Codificacion: "

for i in range(len(codificacion)):
			print '\t',
			for s in range(len(codificacion[i])):
				print repr(codificacion[i][s]).rjust(3)+',',
print '\n'
for i in range(len(codificacion1)):
			print '\t',
			for s in range(len(codificacion1[i])):
				if codificacion1[i][s]<>codificacion[i][s]:
					set_color(color[2])
				print repr(codificacion1[i][s]).rjust(3)+',',
				set_color(0x07)
print '\nDecodificando'
for i in range(len(codificacion1)):
	iden=dot(codificacion1[i],Ht)
	iden=iden.tolist()
	pasarZ(iden,z)
#	print iden
	if iden<>[0,0]:
		a=sindrome.index(iden)
		#print topes[a]
		for u in range(len(codificacion1[i])):
			codificacion1[i][u]=codificacion1[i][u]-topes[a][u]
		pasarZ(codificacion1[i],z)
	decodificacion.append(codificacion1[i][:])
	iden=[]
print decodificacion
for i in range(len(cadena)):
	print cadena[i],
print '\n'
for i in range(len(decodificacion)):
	a=palabras1.index(decodificacion[i])
	if cadena[i]<>letras[a]:
		set_color(color[2])
	print letras[a],
	set_color(0x07)

a=raw_input('\nPulse enter para salir')
