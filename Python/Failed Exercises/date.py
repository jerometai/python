while True:
	print('Enter the first year')
	yearOne = int(input())
	if yearOne <= 1521:
		print()
		print('Please enter a valid year.')
	elif yearOne > 9999:
		print()
		print('Please enter a valid year.')
	elif yearOne <= 9999 > 1521:
		break
print()
while True:
	print('Enter the first month')
	monthOne = int(input())
	if monthOne <= 0:
		print()
		print('Please enter a valid month.')
	elif monthOne >= 13:
		print()
		print('Please enter a valid month.')
	elif monthOne > 0 < 13:
		break
print()
while True:
	print('Enter the first day')
	dayOne = int(input())
	if dayOne <= 0:
		print()
		print('Please enter a valid day.')
	elif dayOne > 31:
		print()
		print('Please enter a valid day.')
	elif dayOne < 32 > 0:
		break
print()
while True:
	print('Enter the second year')
	yearTwo = int(input())
	if yearTwo <= 1521:
		print()
		print('Please enter a valid year.')
	elif yearTwo > 9999:
		print()
		print('Please enter a valid year.')
	elif yearTwo <= 9999 > 1521:
		break
print()
while True:
	print('Enter the second month')
	monthTwo = int(input())
	if monthTwo <= 0:
		print()
		print('Please enter a valid month.')
	elif monthTwo >= 13:
		print()
		print('Please enter a valid month.')
	elif monthTwo > 0 < 13:
		break
print()
while True:
	print('Enter the second day')
	dayTwo = int(input())
	if dayTwo <= 0:
		print()
		print('Please enter a valid day.')
	elif dayTwo > 31:
		print()
		print('Please enter a valid day.')
	elif dayTwo < 32 > 0:
		break
if yearOne > yearTwo:
	firstResy = yearOne - yearTwo
elif yearTwo > yearOne:
	secondResy = yearTwo - yearOne 
if monthOne > monthTwo:
	firstResm = monthOne - monthTwo 
elif monthTwo > monthOne:
	secondResm = monthTwo - monthOne 
if dayOne > dayTwo:
	firstResd = dayOne - dayTwo
elif dayTwo > dayOne:
	secondResd = dayTwo - dayOne 
print()
print(str(firstResy) + ' years, ' + str(firstResm) + ' months, ' + str(firstResd) + ' days ')




