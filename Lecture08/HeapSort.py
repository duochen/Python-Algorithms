from ArrayHeap import ArrayHeap

#######################################################################

h = ArrayHeap()
h.insert(25)
h.insert(14)
h.insert(2)
h.insert(20)
h.insert(10)
h.insert(12)
print(h.data)
for i in range(h.currentsize):
    print(h.deletemin(), end = ' , ')
