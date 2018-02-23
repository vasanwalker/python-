p = input("Input a letter of the alphabet: ")

if p in ('a', 'e', 'i', 'o', 'u'):
	print("%s is a vowel." % p)
elif p == 'y':
	print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
else:
	print("%s is a consonant." % p) 
