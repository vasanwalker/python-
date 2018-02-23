 
m=int(input("Enter number:"))
temp=m
rev=0
while(m>0):
    dig=m%10
    rev=rev*10+dig
    m=m//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
