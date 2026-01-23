from functools import reduce

# def object_of_matches(arr1, arr2, fn):
#     result = {}
#
#     for i, val in enumerate(arr1):
#         if fn(val) == arr2[i]:
#             result[val] = arr2[i]
#
#     return result

def object_of_matches(arr1, arr2, fn):
    def reducer(acc, curr):
        i, val = curr
        if fn(val) == arr2[i]:
            acc[val] = arr2[i]
        return acc

    return reduce(reducer, enumerate(arr1), {})


array1 = ['apple', 'banana', 'cherry', 'date']
array2 = ['APPLE', 'BANANA', 'CHERRY', 'FIG']
numbers1 = [1, 2, 3, 4, 5]
numbers2 = [1, 4, 9, 16, 24]

print(object_of_matches(numbers1, numbers2, lambda x: x * x))

    


# """
#     Construct a function objOfMatches that accepts two arrays and a callback. 
#     objOfMatches will build an object and return it. To build the object, objOfMatches 
#     will test each element of the first array using the callback to see if the output matches 
#     the corresponding element (by index) of the second array. If there is a match, the element from 
#     the first array becomes a key in an object, and the element from the second array becomes the corresponding value.
# """"
