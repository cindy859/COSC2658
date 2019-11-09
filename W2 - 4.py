import math

o = 0

n = int(input("Enter a number: "))
if n > 1:
    for i in range(1, int(math.sqrt(n))):
        o += 1
        if ((n % (6 * i + 1)) or (n % (6 * i - 1))) == 0:
            print(n, "is not a prime number")
            break
    else:
        print(n, "is a prime number")
        print("The number of operation(s) is: ", o)
