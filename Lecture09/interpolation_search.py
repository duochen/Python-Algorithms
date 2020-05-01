def interpolation_search(values, search_for):
    start = 0
    end = len(values) - 1
    while start <= end and search_for >= values[start] and search_for <= values[end]:
        mid = start + \
                int(((float(end - start ) / (values[end] - values [start])) \
                * (search_for - values[start])))
        # Compare the value at mid point with search value
        if values[mid] == search_for:
            return "Found " + str(search_for)+ " at index " + str ( mid )
        if values[mid] < search_for:
            start = mid + 1
    return "Searched element not in the list"

########################################################33

l = [2 , 6 , 11 , 19 , 27 , 31 , 45 , 121]
print(interpolation_search( l, 11 ))           