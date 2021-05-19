l = []
for i in range(5):
	a = input("Dime tu nombre: ")
	b = input("Dime tu apellido: ")
	c = input("Dime tu edad: ")
	d = input("Dime tu altura: ")
	e = input("Dime tu peso: ")
	l.append(a) ; l.append(b) ; l.append(c) ; l.append(d) ; l.append(e)
print(l)
cadena = " ".join(l)
t = cadena.count("a")
p = cadena.count("A")
u = t + p
o = cadena.count("9")
print(u)
print(o)




lista_alumnos=list()

#Introducción de datos
while True:
	nombre=input("Introduce nombre")
	apellido=input("Introduce apellido")
	edad=input("Introduce edad")
	altura=input("Introduce altura")
	peso=input("Introduce peso")
	lista_alumnos.append([nombre,apellido,edad,altura,peso])

	if len(lista_alumnos)>4:
		break

#Contar aes y nueves
num_aes=0
num_9s=0
for fila in lista_alumnos:
	for palabra in fila:
		for i in range(len(palabra)):
			if palabra[i]=="a":
				num_aes=num_aes+1
			if palabra[i]=="9":
				num_9s=num_9s+1

#Mostrar resultados
print("Número de nueves: ", num_9s)
print("Número de aes: ", num_aes)
¡¡