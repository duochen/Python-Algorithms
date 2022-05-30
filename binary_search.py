def binary_search(list, value):
    size = len(list) - 1
    start = 0
    end = size
    # Find the middle most value
    while start <= end:
        mid = (start + end) // 2
        if list[mid] == value:
            return mid
        # Compare the value with the middle most value
        if value > list[mid]:
            start = mid + 1
        else:
            end = mid - 1
    if start > end:
        return None

list = [2, 7, 19, 34, 53, 72]
print(binary_search(list, 72))
print(binary_search(list, 11))