#def double(fn):
#    def result(a):
#        return 2 * fn(a)
#    return result

#@double
#def square(x):
#    return x * x

##print(double(square)(4)) is equivalent to print(square(4))
#print(square(4))

def add_two(fn):
    value = fn(a)
    
    return value + 2

@add_two()
def square(x):
    return x * x

print(square(4))
