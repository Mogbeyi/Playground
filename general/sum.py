def sum_ints(n):
    identity = lambda x: x
    plus = lambda x, y: x + y

    return sum_sequence(n, identity, plus)


def sum_squares_ints(n):
    double = lambda x: x * x
    plus = lambda x, y: x + y

    return sum_sequence(n, double, plus)


def sum_sequence(n, func, combiner):
    if n == 1:
        return 1
    return combiner(func(n), sum_sequence((n - 1), func, combiner))


print(sum_squares_ints(4))
print(sum_ints(4))
