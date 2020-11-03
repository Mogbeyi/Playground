def sum_list(arr):
    if len(arr) == 1:
        return arr[0] 
    return arr[0] + sum_list(arr[1:])

def add_list(arr):
    if len(arr) == 0:
        return 0
    return arr[0][0] + arr[0][1] + add_list(arr[1:])

def count_from_one(x):
     
    def count(start):
        if start > x:
            return []
        return [start] + count(start + 1)

    return count(1)

def count_down(x):
    if x == 0:
        return [0]
    return [x] + count_down(x - 1)

def count_up(x):
    if x == 0:
        return [0]
    else:
        count_arr = count_up(x - 1)
        count_arr.append(x)
    return count_arr

print(count_down(4))
print(count_up(4))
