while True:
	print("Enter '0' for exit.")
	n = int(input("Upto which number ? "))
	if n == 0:
		break
	elif n < 1:
		print("Please, enter a positive number...")
	else:
		sum = 0
		while n > 0:
			sum += n
			n -= 1
		print("Sum = ", sum)
