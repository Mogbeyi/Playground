from reduce import reduce

def intersection_without_reduce(arr1, arr2):
    return [val for val in arr1 if val in set(arr2)]


def intersection_with_reduce(arr1, arr2):
    s2 = set(arr2)

    def keep_if_in_both(accum: list, val):
        if val in s2:
            accum.append(val)
        return accum

    return reduce(arr1, keep_if_in_both, [])

#print(intersection_without_reduce([1,2,3,4,5], [2,4,10,12,5]))
print(intersection_with_reduce([1,2,3,4,5], [2,4,10,12,5]))


