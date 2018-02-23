while True:
	print("Enter '1' for exit.")
	chy = input("Enter any character: ")
	if chy == '1':
		break
	else:
		if((chy>='a' and ch<='z') or (chy>='A' and chy<='Z')):
			print(chy, "is an alphabet.\n")
		else:
			print(chy, "is not an alphabet.\n")
