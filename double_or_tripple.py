def double_or_tripple(f):
    """Returns a function based on the return value of the
       of the function f
    """
    if f(7):
        return lambda x: 2 * x
    else:
        return lambda x: 3 * x

def double(x):
    return x + x 

def minus(x):
    return x - 7 

print(double_or_tripple(double)(4))
print(double_or_tripple(minus)(4))
