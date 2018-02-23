while True:
	print("Enter '0' for exit.")
	chy = input("Enter any character: ")
	if chy == '0':
		break
	else:
		if((chy>='a' and ch<='z') or (ch>='A' and ch<='Z')):
			print(chy, "is an alphabet.\n")
		else:
			print(chy, "is not an alphabet.\n")
