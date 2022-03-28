"""recursive binary search ie a function will call itself to get solution
in recursive binary search list must be sorted """


def recursive_binary_search(list, target):
    if len(list) == 0:                              # checking if the list is empty
        return False
    else:
        midpoint = len(list)//2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
# if midpoint is smaller than the target we will consider right-hand side of the list vice-versa
                return recursive_binary_search(list[midpoint + 1:], target)
# using 'return' to recall the function with new midpoint assign to it
            else:
                return recursive_binary_search(list[:midpoint], target)


def verify(result):
    print(f"is {target} in the list?", result)


numbers = [1, 2, 3, 4, 5, 6, 7]
target = 5
result = recursive_binary_search(numbers, target)
verify(result)
target = 14
result = recursive_binary_search(numbers, target)
verify(result)
print(f"the list is: {numbers}")
