def i(d, e, f):
	a = d * 2
	b = e * 4
	c = f * 4
	g = [a, b, c]
	x = a + b + c
	print(str(g) + ' => ' + str(x) + ' total number of legs.')

while True:
	print()
	print('No. of chickens.')
	d = int(input())
	print()
	print('No. of cows')
	e = int(input())
	print()
	print('No. of pigs.')
	f = int(input())
	i(d, e, f)
	


