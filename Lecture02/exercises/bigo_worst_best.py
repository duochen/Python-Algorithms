def matcher(list, match):
    # Given a list, return a boolean 
    # indicating if match item is in the list

    for item in list:
        if item == match:
            return True
    return False

########################################

lst = [1,2,3,4,5,6,7,8,9,10]
print(matcher(lst,1))
print(matcher(lst,11))