def selectionsort(list):
    for i in range(len(list)):
        idx = i
        for j in range(i + 1, len(list)):
            if list[idx] > list[j]:
                idx = j
        # Swap the minimum value with the compared value
        list[i], list[idx] = list[idx], list[i]

###################################################

list = [84, 21, 96, 15, 47]
print('Original list: ', list)
selectionsort(list)
print('Sorted list: ', list)                    