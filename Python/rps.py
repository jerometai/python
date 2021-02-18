import random

while True:
	x = random.randint(1, 3)
	if x == 1:
		a = 'r'
	elif x == 2:
		a = 'p'
	elif x == 3:
		a = 's'

	if a == 'r':
		c = 'Rock'
	elif a == 'p':
		c = 'Paper'
	elif a == 's':
		c = 'Scissors'

	print()	
	print('Rock, Paper, Scissors. Type r for Rock, p for Paper and s for Scissors and q to Quit.')
	
	while True:
		b = str(input())
		if b == 'r':
			break
		elif b == 'p':
			break
		elif b == 's':
			break
		elif b == 'q':
			break
		elif b != 'r':
			print('Please input a valid move')


	if b == a:
		print()
		print('The opponent used ' + str(c) + '. It\'s a tie!')
	elif b == 'q':
		print()
		print('Thank you for playing, come back again!')
		exit()
	elif a == 'r' and b == 'p':
		print()
		print('Congratulations, the opponent used, ' + str(c) + '. You won!')
	elif a == 'r' and b == 's':
		print()
		print('Unfortunately the opponent used, ' + str(c) + ', you lost.')
	elif a == 's' and b == 'r':
		print()
		print('Congratulations the opponent used, ' + str(c) + '. You won!')
	elif a == 's' and b == 'p':
		print()
		print('Unfortunately the opponent used, ' + str(c) + ', you lost.')
	elif a == 'p' and b == 's':
		print()
		print('Congratulations the opponent used, ' + str(c) + '. You won!')
	elif a == 'p' and b == 'r':
		print()
		print('Unfortunately the opponent used, ' + str(c) + ', you lost.')
	 


