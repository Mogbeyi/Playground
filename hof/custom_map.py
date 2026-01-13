def map(fn, lst):
    result = []

    for val in lst:
        result.append(fn(val))

    return result

print(map(lambda x: x * x, [1,2,3,4,5]))
