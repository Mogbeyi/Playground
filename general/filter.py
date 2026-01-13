# Iterative implementation of filter
def iterative_filter(f, arr):
    if not arr:
        return []

    return [elem for elem in arr if f(elem)]


# Recursive implementation of filter
def recursive_filter(f, arr):
    if not arr:
        return []
    elif f(arr[0]):
        return [arr[0]] + recursive_filter(f, arr[1:])
    else:
        return recursive_filter(f, arr[1:])


def test():
    even = lambda x: x % 2 == 0

    assert iterative_filter(even, [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [2, 4, 6, 8]
    assert recursive_filter(even, [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [2, 4, 6, 8]


test()
