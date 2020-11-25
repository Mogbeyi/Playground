def compose(f, g):

    def compose_result(x):
        return f(g(x))

    return compose_result

add = lambda a: a + 2
multiply = lambda b: b * 2

multiply_and_add = compose(add, multiply)
print(multiply_and_add(10))
