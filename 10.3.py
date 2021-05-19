l = []
while True:
	a = int(input("Pon el numero: "))
	if a >= 0:
		l.append(a)
	else:
		break
for numero in l:
	print(numero , " " , end = "")