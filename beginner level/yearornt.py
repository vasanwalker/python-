while True:
	print("Enter 'x' for exit.")
	n = input("Enter yr: ")
	if n == 'x':
		break
	try:
		yr = int(n)
	except ValueError:
		print("Please, enter yr...")
	else:
		if((yr%4 == 0) and (yr%100 != 0)):
			print(yr, "is a Leap Yr.\n")
		elif(year%100 == 0):
			print(yr, "is not a Leap Yr.\n")
		elif(yr%400 == 0):
			print(yr, "is a Leap Yr.\n")
		else:
			print(yr, "is not a Leap yr.\n")
