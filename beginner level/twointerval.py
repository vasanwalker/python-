low=int(input("Enter the lower limit for the range:"))
upp=int(input("Enter the upper limit for the range:"))
for i in range(low,upp+1):
    if(i%2!=0):
        print(i)
