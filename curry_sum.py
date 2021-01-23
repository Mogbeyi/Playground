def curry_sum(a):
    return lambda b: a + b

print(curry_sum(5)(9))

