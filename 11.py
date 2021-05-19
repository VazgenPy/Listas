l = []
print("Elige (Insertar , Mostrar , Eliminar , Actualizar , Buscar o Salir: ")
while True:
	a = input("Que quieres hacer: ")
	if a == "Insertar" or a == "insertar":
		primero = input("Nom: ")
		segundo = input("Ingredient Principal: ")
		tercero = int(input("Calorias: "))
		cuarto = int(input("Dificauldad (Del 0 al 5): "))
		quinto = input("Explicacion: ")
		l.append([primero,segundo,tercero,cuarto,quinto])
		continue
	elif a == "Mostrar" or a =="mostrar":
		for a in range(len(l)):
			print(l[a])
	elif a == "Eliminar" or a == "eliminar":
		b = int(input("Que elemento quieres eliminar: "))
		l.remove(l[b-1])
	elif a == "Actualizar" or a == "actualizar":
		e = int(input("Que elemento quieres: "))
		f = int(input("Que componente quieres: "))
		g = input("Que quieres poner: ")
		l[e-1][f-1] = g
	elif a == "Buscar" or a == "buscar":
		receta = input("Dime el nombre de la receta: ")
		lista_nueva = []
		falso = False
		for elemento in l:
			for componente in elemento:
				if receta == componente:
					lista_nueva = elemento
					falso = True
		if falso:
			print(lista_nueva)
		else:
			print("No existe")
	elif a == "Salir" or a == "salir":
		print("Adios")
		break