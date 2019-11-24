import random


def generate_random_array_size(length):
    random_array = []

    for i in range(length):
        number = random.randrange(10)  # generates numbers between 0 and 2

        random_array.append(number)

    sort_array = sorted(random_array)

    index1 = random.randint(0, length)

    array1 = sort_array[:index1]
    array2 = sort_array[index1:]
    join_array = array2 + array1

    return join_array


def split_list_pivot(array):
    left = 0
    right = len(array) - 1

    mid = (left + right) // 2
    while left < right:
        if (array[mid] > array[mid - 1]) and (array[mid] > array[mid + 1]):
            return mid + 1
        elif (array[mid] < array[mid - 1]) and (array[mid] < array[mid + 1]):
            return mid
        elif array[mid] >= array[right]:
            left = mid
        else:
            right = mid
        mid = (left + right) // 2


def binary_search(array, target):
    left = 0
    right = len(array) - 1
    mid = (left + right) // 2

    while left <= right:
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            right = mid - 1
        elif array[mid] < target:
            left = mid + 1
        mid = (left + right) // 2

    return -1


def split_list_search(array, target):
    pivot = split_list_pivot(array)
    right = len(array) - 1
    # todo: optimise search by searching left or right array only
    # split original array into sub-arrays
    left_array = array[:pivot]
    right_array = array[pivot:]

    # perform binary search on each sub-array
    left_search = binary_search(left_array, target)
    right_search = binary_search(right_array, target)

    # searching left or right array only
    if array[right] > target and target < array[pivot - 1]:
        left_search
    if array[pivot] > target and target < array[right]:
        right_search

    # return index of the target in the original array
    if (left_search == -1) and (right_search == -1):
        return -1
    elif left_search != -1:
        return left_search
    elif right_search != -1:
        return right_search + pivot


A = generate_random_array_size(5)
print(A)

for i in range(10):
    num = random.randrange(10)
    print(num)
    print("index is", split_list_search(A, num))


