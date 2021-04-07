def binary_search(arr, search_term):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if search_term == guess:
            return 'Found'
        elif guess > search_term:
            high = mid - 1
        else:
            low = mid + 1

    return 'Not Found'

print(binary_search([1,2,3,4,5,6,7,8,9], 2))

