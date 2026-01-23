def for_each(arr:list[any], fn):
    for val in arr:
        print(fn(val))

words = ["dog", "cat", "lion", "jaguar"]
for_each(words, lambda w: w.upper())
