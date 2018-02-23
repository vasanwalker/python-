		
while True:
	print("Enter 'x' for exit.")
	n = input("Enter a number: ")
	if n== 'x':
		break
	else:
		number = int(n)
		if number == 0:
			print("Factorial of 0 is 1\n")
		elif number < 0:
			print("Factorial of negative numbers doesn't exist..!!\n")
		else:
			fact = 1
			for i in range(1, number+1):
				fact = fact*i
			print("Factorial of", number, "is", fact, "\n")
