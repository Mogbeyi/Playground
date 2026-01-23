def reduce(nums: list, fn, accum) -> int:
    for num in nums:
        accum = fn(accum, num)

    return accum

def test():
    print(reduce([1,2,3,4], lambda a, b: a + b, 0))
    print(reduce([1,2,3,4], lambda a, b: a * b, 1))
