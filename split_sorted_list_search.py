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

    # todo: optimise search by searching left or right array only
    # split original array into sub-arrays
    left_array = array[:pivot]
    right_array = array[pivot:]

    # perform binary search on each sub-array
    left_search = binary_search(left_array, target)
    right_search = binary_search(right_array, target)

    # return index of the target in the original array
    if (left_search == -1) and (right_search == -1):
        return -1
    elif left_search != -1:
        return left_search
    elif right_search != -1:
        return right_search + pivot


A = [23, 100, 103, 103, 105, 3, 5, 8, 10, 11, 11, 13, 20]
B = [23, 100, 103, 103, 105]

print(split_list_search(A, 103))
