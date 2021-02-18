print('What is your name?')
myName = input()
print()
print('It is nice to meet you, ' + myName)
print('')
print('The length of your name is:')
print(len(myName))
print()
print('How old are you?')
myAge = input()
print()
print('You will be ' + str(int(myAge) + 1) + ' years old next year.')
print()
print('This time, the script will ask you to input two numbers, and both of them will be added together. Easy, right?')
print('Press Enter To Continue...')
dummyTwo = input()
print('Alright, type in your first number.')
firstNum = float(input())
print()
print('Good job, next, your second number.')
secondNum = float(input())
sum = int(firstNum) + int(secondNum)
print()
print('The sum is ' + str(sum))
print()
print('If you can input the correct password, then you may proceed.')
while True:
	myPass = input()
	print()
	if myPass == 'Jerome':
		break
	else:
		print('Incorrect Password: Access Denied, Try again.')
print('ACCESS GRANTED: Welcome Back, Tai Jerome C.')




















