import math

def prime_checker(number):
    assert number > 1, 'number needs to be greater than 1'
    number_of_operations = 0
    if number % 2 == 0 or number % 3 == 0:  #need to check with prime number 2 and 3 too
        number_of_operations += 4  #number mod 2 and 3, 2 comparisons
        print(number, "is not a prime number")
    else:
        for i in range(5, int(math.sqrt(number))):
            number_of_operations += 8  #i increment, square root number, multiplication, subtraction, 2 mod, 2 compare
            if (i * i - 1) % 24 == 0:
                if number % i == 0:
                    return False, number_of_operations  # returning multiple values (as a tuple)
    return True, number_of_operations  # returning multiple values (as a tuple)


numbers = [373, 149573, 1000033, 6700417]
for number in numbers:
    (is_prime, number_of_operations) = prime_checker(number)
    if is_prime:
        print(number, "is prime")
    else:
        print(number, "is not prime")
    print('Number of operations:', number_of_operations)
    print('')

