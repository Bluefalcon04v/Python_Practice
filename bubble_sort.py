'''in bubble sort we iterate numbers while swapping.
going to print ascending order and descending order list using bubble sort'''

def sort_descending(list):
    for i in range(len(list)-1):
        for j in range(len(list)-1-i):
            if list[j] < list[j + 1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp


def sort_ascending(list):
    for i in range(len(list)-1):
        for j in range(len(list)-1-i):
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp


list = [13, 1, 9, 60, 55, 32, 8, 72, 33, 4]
print("original list: ", list)
sort_descending(list)
print("descending order: ", list)
sort_ascending(list)
print("ascending order: ", list)

