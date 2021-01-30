def action(fn, x):
    return fn(x)

inc = lambda x: x + 1
square = lambda x: x * x

print(action(inc, 42))
print(action(square, 8))
