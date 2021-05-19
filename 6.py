import random 
#Cracion De La Matriz
l = [[],[],[],[],[]]
for i in range(5):
	for a in range(5):
		l[i].append(random.randint(1,100))
	print(l[i])
#Suma De Filas
for f in range(5):
	print("suma de la fila" , f+1 , ":" , sum(l[f]))
#Suma de Columnas
c1 = [] ; c2 = [] ; c3 = [] ; c4 = [] ; c5 = []
for c in range(5):
	c1.append(l[c][0])
	c2.append(l[c][1])
	c3.append(l[c][2])
	c4.append(l[c][3])
	c5.append(l[c][4])
print("La suma de la columna 1: " , sum(c1)) 
print("La suma de la columna 2: " , sum(c2))  
print("La suma de la columna 3: " , sum(c3)) 
print("La suma de la columna 4: " , sum(c4)) 
print("La suma de la columna 5: " , sum(c5))
#Suma De Diagonal 1
d1 = []
for d in range(5):
	d1.append(l[d][d])
print("La suma de la diagonal es: " , sum(d1))
#Suma De Diagonal 2
d2 = []
for e in range(5):
	d2.append(l[4-e][e])
print("La suma de la diagonal 2 es: " , sum(d2))