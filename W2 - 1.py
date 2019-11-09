# cook your dish here

o = 0

n = int(input("Enter a number: "))  
  
if n > 1:  
   for i in range(2,n):
       o+=1
       if (n % i) == 0:  
           print(n,"is not a prime number")  
           break  
   else:  
       print(n,"is a prime number")  
       print("The number of operation(s) is: ",o)
