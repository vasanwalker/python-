a=[]
m=int(input("Enter number of elements:"))
for i in range(1,m+1):
    b=int(input("Enter element:"))
    a.append(b)
a.sort()
print("Largest element is:",a[m-1])
