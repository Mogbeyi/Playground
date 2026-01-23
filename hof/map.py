def map(nums:list[int], fn) -> list[int]:
    return [fn(num) for num in nums]

print(map([1,2,3,4], lambda x: x * x))

