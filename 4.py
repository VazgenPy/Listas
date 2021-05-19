l = []
w = []
for i in range(5):
	l.append(input("Pon un caracter: "))
for i in range(len(l)):
	w.append(l[i])
w.reverse()
print(w)