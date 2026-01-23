from for_each import for_each

def map_with(arr, fn):
    result = []
    for_each(arr, lambda x: result.append(fn(x)))
    return result

print(map_with([1, 2, 3, 4], lambda x: x * x))
