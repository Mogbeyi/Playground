def filter(fn, lst):
    return [val for val in lst if fn(val)]

print(filter(lambda x: x % 2 == 0, [1,2,3,4,5,6,7,8]))
