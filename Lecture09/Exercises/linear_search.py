def linear_search(values, search_for):
    search_at = 0
    is_found = False

    while search_at < len(values) and is_found is False:
        if values[search_at] == search_for:
            is_found = True
        else:
            search_at = search_at + 1

    return is_found

###################################################

l = [64, 34, 25, 12, 22, 11, 90]
print(linear_search(l, 12))
print(linear_search(l, 91))