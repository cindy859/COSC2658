# I'm gonna be fairly nit-picking just to warn ya
# Overall the logic is fine
# But this would require you to manually input every number and manually record the number of operations
# Why not automate that?

# todo: make the variable name descriptive please, not too big of a problem for a small program but boi it can be a mess
# todo: I suggest changing this to sth like "number_of_operations"
o = 0

# todo: better variable name
n = int(input("Enter a number: "))

if n > 1:
    for i in range(2, n):
        o += 1
        if (n % i) == 0:
            print(n, "is not a prime number")
            break
    else:
        print(n, "is a prime number")
        print("The number of operation(s) is: ", o)
