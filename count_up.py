#Returns a list in the range start to end

#Iterative implementation
def count_up(start, end):
    count = []

    for num in range(start, end + 1):
       count += [num] 

    return count

#Tail recursive implementation
def count_up_two(start, end):

    def count_up_tail_recursive(start, end, count_list):
        if start > end:
            return count_list
        return count_up_tail_recursive(start + 1, end, count_list + [start])

    return count_up_tail_recursive(start, end, [])

# Curried Implementation
def count_up_to(end):

    def start_value(start):
        result = []

        for num in range(start, end + 1):
            result.append(num)

        return result
    
    return start_value

def test():

    assert(count_up(1, 7)) == [1,2,3,4,5,6,7]
    assert(count_up_two(1, 7)) == [1,2,3,4,5,6,7]
    assert(count_up_to(7)(3)) == [3,4,5,6,7]

test()
