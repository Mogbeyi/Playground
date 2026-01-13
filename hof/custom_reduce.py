def custom_reduce(fn, lst, start=None):
    iter_lst = iter(lst)

    if not start:
        accumulator = next(iter_lst)
    else:
        accumulator = start

    for val in iter_lst:
        accumulator = fn(accumulator, val)

    return accumulator

print(custom_reduce(lambda a, b: a + b, [1,2,3,4,5]))
print(custom_reduce(lambda a, b: a * b, [1,2,3,4]))
