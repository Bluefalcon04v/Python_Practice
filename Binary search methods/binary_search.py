"""in this we will keep cutting down the list in half till we get our target value"""

position = 0
def search(list, target):
    l = 0
    u = len(list) - 1
    list.sort()                         # list must be sorted to perform binary search operation
    print ('sorted list in ascending order:', list)

    while l <= u:
        mid = (l + u) // 2
        if list[mid] == target:
            globals()['position'] = mid
            return True
        else:
            if list[mid] < target:
                l = mid + 1             # changing "l" to mid+1 because mid_value is less than target value
            else:
                u = mid - 1             # changing "u" to mid+1 because mid_value is greater than target value
    return False


list = [20, 4, 6, 8, 12, 10, 18, 14, 16, 18, 2]
target = 8
if search(list, target):
     print(f"found {target} and it's position is ", position+1)
else:
    print("not found")