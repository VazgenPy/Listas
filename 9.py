l = []
for i in range(2):
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
o = cadena.count("9")
print("Numero de A" , t+p)
print("Numero de 9" , o)

# localizar palabra

nombre = input("Dime el nombre: ")

eleccion = input("Que quieres (apellido , edad , altura , peso): ")

for persona in range(len(l)):
	for palabra in l[persona]:
		if eleccion == "apellido":
			print(palabra[1])
	for palabra in range(len(l)):
		if eleccion == "edad":
			print(l[persona])
	for palabra in l[persona]:
		if eleccion == "altura":
			print(palabra[3])
	for palabra in l[persona]:
		if eleccion == "peso":
			print(palabra[4])