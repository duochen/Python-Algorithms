def print_comp(lst):
    # This function prints the first item O(1)
    # Then is prints the first 1/2 of the list O(n/2)
    # Then prints a string 10 times O(10)
    print(lst[0])

    midpoint = round(len(lst)/2)

    for val in lst[:midpoint]:
        print(val)

    for x in range(10):
        print("number")

#######################################

print_comp([1,2,3,4,5,6,7,8,9,10])