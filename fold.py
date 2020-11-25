# Tail recursive implemention of the functional programming fold feature
def tail_recursive_fold(f, acc, arr):
    if not arr:
        return acc 
    return tail_recursive_fold(f, f(acc, arr[0]), arr[1:])

def test():
    assert(tail_recursive_fold(lambda a, b: a + b, 0, [1,2,3,4,5])) == 15
    assert(tail_recursive_fold(lambda a, b: a * b, 1, [1,2,3,4,5])) == 120 

test()
