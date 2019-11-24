def min_sum_pair(array):
    sum_of_pair = 0
    min_sum = 1000

    left = 0
    right = len(array) - 1

    min_left = 0
    min_right = len(array) - 1

    while left < right:
        sum_of_pair = array[left] + array[right]

        if abs(sum_of_pair) < abs(min_sum):
            min_sum = sum_of_pair
            min_left = left
            min_right = right
        if sum_of_pair < 0:
            left += 1
        else:
            right -= 1

    print("Two integers in the array whose sum is closest to zero is",
          array[min_left], "and", array[min_right])


arr = [-10, -9, -8, -7, 1, 2, 10, 12]
min_sum_pair(arr)
