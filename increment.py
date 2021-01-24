def action(fn, x):
    return fn(x)

print(action(lambda x: x + 1, 42))
print(action(lambda x: x * x, 8))

