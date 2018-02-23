while True:
	print("Enter 'x' for exit.")
	n = input("Enter any number: ")
	if n == 'x':
		break
	try:
		number = int(n)
	except ValueError:
		print("Please, enter a number...")
	else:
		for i in range(2, number):
			if number%i == 0:
				print(number, "is not a prime number.\n")
				break
		else:
			print(number, "is a prime number.\n")
