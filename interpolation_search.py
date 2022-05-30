def interpolation_search(values, search_for):
    start = 0
    end = len(values) - 1
    while start <= end and search_for >= values[start] and search_for <= values[end]:
        probe = start + \
            int(((float(end-start) / (values[end] - values[start])) \
                * (search_for - values[start])))
        # Compare teh value at the mid point with search value
        if values[probe] == search_for:
            return "Found " + str(search_for) + " at index " + str(probe)
        if values[probe] < search_for:
            start = probe + 1
        if values[probe] > search_for:
            end = probe - 1
    return "Searched element not in the list"



l = [2, 6, 11, 19, 27, 31, 45, 121]
print(interpolation_search(l, 11))