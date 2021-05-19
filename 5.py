l = []
for i in range(1 , 7):
	print("Dia" , i)
	l.append(int(input("dime la temperatura minima: ")))
	l.append(int(input("dime la temperatura maxima: "))) 
print("La media es :" , sum(l)/12)
print("La maxima es: ", max(l))   
print("La minima es: ", min(l))