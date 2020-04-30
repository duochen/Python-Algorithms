def insertionsort(list):
    for i in range(1, len(list)):
        value = list[i]
        position = i

        while position > 0 and list[position - 1] > value:
            list[position] = list[position-1]
            position = position - 1

        list[position] = value

###################################################

list = [84, 21, 96, 15, 47]
print('Original list: ', list)
insertionsort(list)
print('Sorted list: ', list)