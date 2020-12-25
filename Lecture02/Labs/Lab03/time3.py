def BinarySearch(mylist, item):
    low = 0
    high = len(mylist)-1
    while low <= high:
        mid = (low+high)/2
        if item == mylist[mid]:
            return mid+1
        elif item<mylist[mid]:
            high=mid-1
        else:
            low=mid+1

    return -1
