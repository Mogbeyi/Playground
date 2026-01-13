def pair_sum_sequence(n):
    total = 0

    pair_sum = lambda a, b: a + b

    for i in range(n):
        total += pair_sum(i, i + 1)

    return total 

def test():
    assert pair_sum_sequence(2) == 4
    assert pair_sum_sequence(3) == 9
    assert pair_sum_sequence(4) == 16 

test()
