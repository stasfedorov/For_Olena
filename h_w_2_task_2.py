#1

a = 179
b = 971
c = (a ** 2 + b ** 2) ** (0.5)
print('c =', c)

#1b

import math
c = math.sqrt((a ** 2 + b ** 2))
print('c =', c)

#2

d = 45
print(d // 10)

#3

e = 123456789
f = str(e)
g = 0
for i in f:
	g = g + int(i)
print(g)

#4

h = 23
if 23 // 2 == 0:
	print(h + 2)
else: 
	print(h + 1)
	
#5

j = 123.1234567
print(j - int(j))

#5b

j = 123.1234567
print(j % 1)

#6

k = 1234.1234
print(int(k*10)%10)


