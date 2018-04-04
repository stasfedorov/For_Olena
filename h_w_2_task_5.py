a = 3
b = 2
c = 1
if a >= b and b >= c:
	a, b, c = c, b, a
elif a>=c and c >=b:
	a, b, c = b, c, a
elif b >= a and a >= c:
	a, b, c = c, a, b
elif b >= c and c >= a:
	a, b, c = a, c, b
elif c >= a and a >= b:
	a, b, c = b, a, c
print(a, b, c)