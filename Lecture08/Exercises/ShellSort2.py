def shellsort(list):
    gap = len(list) // 2
    while gap > 0:
        for i in range(gap, len(list)):
            temp = list [i]
            j = i
            # Sort the sub list for this gap
            while j >= gap and list [j - gap] > temp:
                list [j] = list [j - gap]
                j = j - gap
            list [j] = temp
        # Reduce the gap for the next element
        gap = gap // 2

###################################################

list = [84, 21, 96, 15, 47]
print('Original list: ', list)
shellsort(list)
print('Sorted list: ', list)                        