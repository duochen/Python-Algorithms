a = {
    'x': 1,
    'y': 2,
    'z': 3
}
b = {
    'w': 10,
    'x': 11,
    'y': 2
}

# Find keys in common
result = a.keys() & b.keys() # { 'x', 'y' }
print(result)
# Find keys in a that are not in b
result = a.keys() - b.keys() # { 'z' }
print(result)
# Find (key,value) pairs in common
result = a.items() & b.items() # { ('y', 2) }
print(result)