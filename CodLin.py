from numpy import *
import random

# -*- coding: utf-8 -*-
#
#       CODLIN.py
#       
#       Copyright 2012 Carlos Jesus Fernandez Basso <cjferba@gmail.com>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#       
#      



"""
Funcion nor(x1)
Funcion que normaliza una matriz mediante 
el Algoritmo de normalizacion de matrices
"""
def nor(x1):
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
						a=x[i][d]*x[s][d]
						x[s][d]=x[s][d]-a
	return x[:]
#		for ww in range(f):
#			print x[ww]
#		print '\n'



def buscar(x,i):
#busca en matriz X desde la posicion m[i][i] un valor inferior para cambiarlo sino busca por columnas
	c=len(x)-(i+1)
	for s in range(c):
			if x[s+i][i]<>0:
				return [s+i]

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

matriz=[]#matrix[Filas][Columnas]
iden=[]
m1=[]
n=int(raw_input("matriz filas:"))
m=int(raw_input("matriz columnas:"))
for i in range(n):
	for x in range(m):
		if(x==i):
			m1.append(1)
		else:
			m1.append(random.randint(1,5))
	matriz.append(m1[:])
	m1=[]
matriz[0][0]=0
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
v=[]
v=array([1,1,1,1])
print "Identidad\t\t*(Por)\n",
for i in range(len(iden)):
	for x in range(len(iden[i])):
		print iden[i][x],
	if i==len(iden)/2:
		print"     \t\t", v,
	print "\n"
#multiplicamos mediante dot de numpy
m1=dot(iden,v)
#convertimos el array a lista 
m1=m1.tolist ()
imprimir(m1)
print "\nSolucion Normalizacion"
m1=nor(matriz)
imprimir(m1)
raw_input("")









