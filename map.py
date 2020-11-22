def my_map(f, arr):
    if not arr:
        return arr
    return [f(arr[0])] + my_map(f, arr[1:])

add_one = lambda x: x + 1
first = lambda x: x[0]

print(my_map(add_one, [1,2,3,4]))
print(my_map(first, [[32,4,2,3], [1,2,3,4], [3,2,4,2], [1,3,4,5]]))

