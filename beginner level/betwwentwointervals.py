
low = 900
upp = 1000


print("Prime numbers between",low,"and",upp,"are:")

for n in range(low,upp + 1):
   # prime numbers are greater than 1
   if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
               break
       else:
           print(n)
