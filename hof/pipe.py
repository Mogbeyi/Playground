from functools import reduce

# def pipe(arr, val):
#     result = val
#
#     for fn in arr:
#         result = fn(result)
#
#     return result
#

def pipe(arr, val):
    return reduce(lambda accum, fn: fn(accum), arr, val)

functions = [
    lambda x: x + x,
    lambda x: x * x,
    lambda x: x
]

print(pipe(functions, 2))


