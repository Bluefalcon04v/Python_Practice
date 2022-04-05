"""identifying the greatest number in the sorted list using binary search technique """


def binary_search(numbers, lower=0, upper=10):

    mid = (lower + upper)//2            # search for middle index of the list
    mid_value = numbers[mid]            # assigning middle index number to mid_value
    while lower < upper:
        if mid_value < numbers[mid - 1]:
            new_upper = mid - 1         # assigning new upper in binary search function again
            return binary_search(numbers, lower, new_upper)
        elif mid_value < numbers[mid + 1]:
            new_lower = mid + 1         # assigning new lower in binary search function again
            return binary_search(numbers, new_lower, upper)

    print("The greatest number in the list is", mid_value)


numbers = [2, 4, 6, 7, 10, 12, 14, 17, 18, 21, 22]
binary_search(numbers)