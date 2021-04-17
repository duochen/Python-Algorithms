dict1 = {'a':1}
dict2 = dict1.copy()
dict2['a'] = 2
dict3 = dict(dict1)
dict3['a'] = 9
print(dict1)
print(dict2)
print(dict3)