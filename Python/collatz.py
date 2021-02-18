def collatz(a):
	if (a % 2) == 0:
		print(a // 2)
		return a // 2
	elif (a % 2) != 0:
		b = 3 * a + 1
		print(b)
		return b
			
print('Input')
try:
	a = int(input())
except NameError: 
	print('Please enter a valid integer.')
except ValueError:
	print('Please enter a valid integer.')
while a != 1:
	a = collatz(a)
print('Algorithm Solved.')
