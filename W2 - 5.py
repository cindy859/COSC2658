import math

o = 0

n = int(input("Enter a number: "))
if n > 1:
    for i in range(5, int(math.sqrt(n))):
        o += 1
        if (n % (i * i - 1) % 24) == 0:
            print(n, "is not a prime number")
            break
    else:
        print(n, "is a prime number")
        print("The number of operation(s) is: ", o)
