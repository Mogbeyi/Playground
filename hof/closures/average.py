def average():
    nums = []

    def wrapper(*args):
        nonlocal nums
        if args:
            nums.append(args[0])
            print(sum(nums) / len(nums))
        else:
            print(sum(nums) / len(nums))

    return wrapper


test_average = average()
test_average(0)
