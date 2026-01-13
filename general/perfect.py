#def increment_n_times(n, x):
#    if n == 0:
#        return x
#    print(x)
#    return 1 + increment_n_times(n - 1, x)
#

#def double_n_times(n, x):
#    if n == 0:
#        return x
#    return 2 * double_n_times(n - 1, x)
#

#def nth_tail(n, xs):
#    if n == 0:
#        return xs
#    return nth_tail(n - 1, xs[1:])
#

def process(combiner, n, x):
    if n == 0:
        return x 
    return combiner(process(combiner, n - 1, x)) 

increment = lambda x: x + 1
double = lambda x: 2 * x
tail = lambda xs: xs[1:]

#def increment_n_times(n, x):
#    return process(increment, n, x)
#

def double_n_times(n, x):
    return process(double, n, x)

def nth_tail(n, xs):
    return process(tail, n, xs)

print(increment_n_times(5, 5))
#print(double_n_times(3, 2))
#print(nth_tail(2, [4, 8, 12, 16]))
#
