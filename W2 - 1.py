def prime_checker(number):
    assert number > 1, 'number needs to be greater than 1'

    number_of_operations = 0
    for i in range(2, number):
        number_of_operations += 3  #increase of i, number mod i, comparision
        if (number % i) == 0:
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
