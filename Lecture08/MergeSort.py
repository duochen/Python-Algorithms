def mergesort(list):
    if len(list) > 1:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]

        mergesort(left)
        mergesort(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i = i + 1
            else:
                list[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            list[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            list[k] = right[j]
            j = j + 1
            k = k + 1

###################################################

list = [84, 21, 96, 15, 47]
print('Original list: ', list)
mergesort(list)
print('Sorted list: ', list)            