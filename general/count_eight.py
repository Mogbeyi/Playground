#count the number of times 8 occurs in an integer
def count_eight(x):
    if x % 10 == 8:
        return 1 + count_eight(x // 10)
    elif x < 10:
        return 0
    else:
        return count_eight(x // 10)

def test():
    assert count_eight(8338) == 2
    assert count_eight(888) == 3
    assert count_eight(7778) == 1
    assert count_eight(648236) == 1
    assert count_eight(77777) == 0
    assert count_eight(88888) == 5
    assert count_eight(8) == 5

test()

