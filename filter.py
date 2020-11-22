#Iterative implementation of filter
def iterative_filter(f, arr):
    if not arr:
        return []

    filter_result = []

    for elem in arr:
        if f(elem):
            filter_result.append(elem)

    return filter_result

#Recursive implementation of filter
def recursive_filter(f, arr):
    if not arr:
        return []
    elif f(arr[0]):
        return [arr[0]] + recursive_filter(f, arr[1:])
    else:
        return recursive_filter(f, arr[1:])

def test():
    even = lambda x: x % 2 == 0

    print(iterative_filter(even, [1,2,3,4,5,6,7,8,9]))
    print(recursive_filter(even, [1,2,3,4,5,6,7,8,9]))

test()
