import random

a = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')
print('Take a guess.')
while True:
	b = int(input())
	if b < a:
		print('Your guess is lower.')
	elif b > a:
		print('Your guess is higher.')
	elif a == b:
		break
print()
print('Congratulations, you guessed the secret number! It was ' + str(a) + '.')


