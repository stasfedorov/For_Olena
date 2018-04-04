#1st

while True:
	inp = input('Enter the year\n> ')
	if inp == 'done':
		break
	year = int(inp)
	if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
		print('YES')
	else:
		print('NO')
		
#2nd

import calendar
inp_year = input('Enter the year\n> ')
year_1 = int(inp_year)
if calendar.isleap(year_1) == True:
	print('Yes')
else:
	print('No')
	