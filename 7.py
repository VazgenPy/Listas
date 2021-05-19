l = [[],[],[],[],[]]
for i in range(1):
	for a in range(10):
		l[i].append("1")
for i in range(1,2):
	for a in range(1):
		l[i].append("1")	
	for a in range(1,9):
		l[i].append("0")	
	for a in range(9,10):
		l[i].append("1")
for i in range(2,3):
	for a in range(1):
		l[i].append("1")	
	for a in range(1,9):
		l[i].append("0")	
	for a in range(9,10):
		l[i].append("1")
for i in range(3,4):
	for a in range(1):
		l[i].append("1")	
	for a in range(1,9):
		l[i].append("0")	
	for a in range(9,10):
		l[i].append("1")
for i in range(4,5):
	for a in range(10):
		l[i].append("1")
print(l[0] , "\n" , l[1] , "\n", l[2] , "\n" , l[3] , "\n" , l[4])
