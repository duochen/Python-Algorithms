import heapq

h = [21, 1, 45, 78, 3, 5]
print(h)

# Use heapify to rearrange the elements
heapq.heapify(h)
print(h)

# Repalce an element
heapq.heapreplace(h, 6)
print(h)