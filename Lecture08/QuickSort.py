def quicksort(list, low, high):
    if low < high:
        p = partition(list, low, high)
        quicksort(list, low, p-1)
        quicksort(list, p+1, high)

def partition(list, low, high):
    i = low - 1
    pivot = list[high]
    for j in range(low, high):
        if list[j] <= pivot:
            i = i + 1
            list[i], list[j] = list[j], list[i] 

    list[i+1], list[high] = list[high], list[i+1]

    return i+1

###################################################

list = [84, 21, 96, 15, 47]
print('Original list: ', list)
quicksort(list, 0, len(list)-1)
print('Sorted list: ', list)                