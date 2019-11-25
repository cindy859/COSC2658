arr = [5, 10, 15, 20, 25, 30, 35]


def binary_search_for_distributed_array(array, x):
    low = 0
    high = len(array) - 1
    position = low + ((x - array[low]) * (high - low) // (array[high] - array[low]))

    if x > array[high]:
        return -1

    while low < high:
        if array[position] == x:
            return position
        elif array[position] > x:
            low = position + 1
        elif array[position] < x:
            high = position - 1


print(binary_search_for_distributed_array(arr, 40))



