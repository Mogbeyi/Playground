def f(x, y, z):
    square = lambda num: num * num

    return square(x) + square(y) + square(z) - min(square(x), square(y), square(z))

def test():
    assert f(1,2,3) == 13
    assert f(2,3,4) == 25

test()
