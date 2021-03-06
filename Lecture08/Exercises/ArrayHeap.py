from ArrayHeapError import ArrayHeapError

class ArrayHeap:
    def __init__(self):
        self.maxsize = 10
        self.data = [-1] * self.maxsize
        self.currentsize = 0

    def len(self):
        return len(self.data)

    def is_empty(self):
        return self.len() == 0

    def max(self):
        if self.currentsize == 0:
            raise ArrayHeapError('Heap is empty')
        return self.data[1]
    
    def insert(self, e):
        if self.currentsize == self.maxsize:
            raise ArrayHeapError('No space')
        self.currentsize += 1
        i = self.currentsize
        while i != 1 and e < self.data[i//2]:
            self.data[i] = self.data[i//2]
            i = i // 2
        self.data[i] = e

    def deletemin(self):
        if self.currentsize == 0:
            raise ArrayHeapError('Heap is empty')
        x = self.data[1]
        y = self.data[self.currentsize]
        self.currentsize -= 1
        i = 1
        ci = 2
        while ci <= self.currentsize:
            if ci < self.currentsize and self.data[ci] > self.data[ci+1]:
                ci += 1
            if y <= self.data[ci]:
                break
            self.data[i] = self.data[ci]
            i = ci
            ci = ci * 2
        self.data[i] = y
        return x