import json


def max_sum(array):
    n = len(array)
    maximum_sum = array[0]
    current_sum = array[0]
    for e in range(1, n):
        current_sum = max(current_sum + array[e], array[e])
        maximum_sum = max(maximum_sum, current_sum)

    return maximum_sum


arr1 = [3, 4, -9, 1, 2, 5]
result = max_sum(arr1)
print(result)
