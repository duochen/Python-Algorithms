def bubblesort(list):
    for i in range(len(list)-1, 0, -1):
        for j in range(i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

###################################################

list = [84, 21, 96, 15, 47]
print('Original list: ', list)
bubblesort(list)
print('Sorted list: ', list)
