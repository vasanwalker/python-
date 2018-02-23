while True:
	print("Enter 'x' for exit.")
	print("Enter any three numbers: ")
	n1 = input()
	n2 = input()
	n3 = input()
	if n1 == 'x':
		break
	else:
		number1 = int(n1)
		number2 = int(n2)
		number3 = int(n3)
		largest = number1
		if largest < number2:
			if number2 > number3:
				largest = number2
			else:
				largest = number3
		elif largest < number3:
			if number3 > number2:
				largest = number3
			else:
				largest = number2
		else:
			largest = number1
		print("Largest of given three numbers is",largest,"\n")
