def summation(fn, num):
    if num == 1:
        return 1
    return fn(num) + summation(fn, num - 1)

def identity_sum(n):
    return summation(lambda x: x, n)

def square_sum(n):
    return summation(lambda x: x * x, n)


def build_summation(fn):

    def inner_func(n):
        if n == 1:
            return 1
        return fn(n) + inner_func(n -1)

    return inner_func

sum_integers = build_summation(lambda x: x)
sum_squares = build_summation(lambda x: x * x)

print(sum_squares(4))
