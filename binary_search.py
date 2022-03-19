"""searching number efficiently using binary search technique ie. using mid value for search,
 from an unorganised list."""

posn = 0

def search(list, n):
    l = 0
    u = len(list) - 1
    list.sort()               #in binary search sorting list is an important step. 
    print ('sorted list in ascending order:', list)

    while l <= u:
        mid = (l + u) // 2
        if list[mid] == n:
            globals()['posn'] = mid
            return True
        else:                 #"n" > or < than "mid" value
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid - 1
    return False

list = [20, 4, 6, 8, 12, 10, 18, 14, 16, 18, 2]
n = 8
if search(list, n):
     print(f"found {n} and it's position is ", posn+1)
else:
    print("not found")
