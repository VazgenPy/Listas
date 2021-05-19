import random
l = []
for i in range(10):
	l.append(random.randint(1 , 10))
for numero in l:
	print(numero , numero ** 2 , numero ** 3)
