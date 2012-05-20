from numpy import *

##Algoritmo de normalizacion de matrices##
def nor(x):
        f=len(x)
        c=len(x[0])
        for i in range(f):
                if x[i][i]==0:
                        print"OK"
                elif x[i][i]<>0:
                        for s in range(c):
                                x[i][s]=x[i][s]*1/x[i][i]
                else:
                        #buscar
                        print ""
def buscar(x,i):
#busca en matriz X desde la posicion m[i][i] un valor inferior para cambiarlo sino busca por columnas
	c=len(x)-i
	for s in range(c):
			if x[s+i][i]<>0:
				return [s+i]
                
########MAIN############
                
matriz=[]#matrix[Filas][Columnas]
iden=[]
m1=[]
n=int(raw_input("matriz filas:"))
m=int(raw_input("matriz columnas:"))
for i in range(n):
	for x in range(m):
		m1.append(1)
	matriz.append(m1[:])
	m1=[]
n=int(raw_input("iden filas:"))
m=int(raw_input("iden columnas:"))
for i in range(n):
	for x in range(m):
		if(x==i):
			m1.append(1)
		else:
			m1.append(0)
	iden.append(m1[:])
	m1=[]

print "Matriz"
for i in range(len(matriz)):
	for x in range(len(matriz[i])):
		print matriz[i][x],
	print "\n"

print "Identidad",
for i in range(len(iden)):
	for x in range(len(iden[i])):
		print iden[i][x],
		print "\n"
v=[]
v=array([1,1,1,1])
m1=dot(matriz,v)
print "Sol",m1[1]

for i in range(len(m1)):
		for x in range(len(m1[i])):
			print m1[i][x],
		print "\n"
raw_input("")









