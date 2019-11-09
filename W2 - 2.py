# cook your dish here

o = 0

n = int(input("Enter a number: "))  
i = 3
if n > 1: 
   while i <= int(n/2): 
       o+=1
       if (n % i) == 0:  
           print(n,"is not a prime number")  
           break  
       i+=2
   else:  
       print(n,"is a prime number")  
       print("The number of operation(s) is: ",o)