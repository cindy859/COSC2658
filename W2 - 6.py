def fibs(n):
    array = [None] * n
    array[0] = 0
    array[1] = 1
    for i in range(2, n):
        array[i] = array[i - 1] + array[i - 2]
    return array


fib_numbers = fibs(2000)
first_digit_counts = [0] * 10
last_digit_counts = [0] * 10

for number in fib_numbers:
    first_digit = int(str(number)[0])
    last_digit = int(str(number)[-1])

    first_digit_counts[first_digit] += 1
    last_digit_counts[last_digit] += 1

print(first_digit_counts)
print(last_digit_counts)

