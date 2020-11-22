#Iterative implementation of filter
def filter(f, arr):
    if not arr:
        return []

    filter_result = []

    for elem in arr:
        if f(elem):
            filter_result.append(elem)

    return filter_result

even = lambda x: x % 2 == 0

print(filter(even, [1,2,3,4,5,6,7,8,9]))
