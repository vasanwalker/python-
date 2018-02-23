while True:
	print("Enter 'n' for exit.")
	n = input("Enter any number: ")
	if n == 'x':
		break
	else:
		number = int(n)
		tot = 0
		temp = number
		while temp > 0:
			dig = temp % 10
			tot += dig ** 3
			temp //= 10
		if number == tot:
			print(number,"is an Armstrong Number.\n")
		else:
			print(number,"is not an Armstrong Number.\n")
