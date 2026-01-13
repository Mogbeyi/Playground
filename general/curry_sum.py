def curry_sum(a):
    return lambda b: a + b

for i in range(10):
    print(curry_sum(5)(i))


