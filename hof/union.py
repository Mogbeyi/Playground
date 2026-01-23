from functools import reduce

def union(*arr):
    arrs = list(arr)
    check_for_union = lambda a, b: set(a) | set(b)

    return list(reduce(check_for_union, arrs))

print(union([1,2,3,4], [5,6,7]))


