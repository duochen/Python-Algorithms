class ArrayQueue:
    def __init__(self):
        self.data = []
        self.size = 0
        self.front = 0
        
    def is_empty(self):
        return self.size == 0
    
    def enqueue(self, e):
        self.data.append(e)
        self.size = self.size + 1
        
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        value = self.data[self.front]
        self.data[self.front] = None
        self.front = self.front + 1
        self.size = self.size - 1
        return value
    
    def first(self):
        if self.is_empty():
            print("Queue is empty")
        return self.data[self.front]
    
s = ArrayQueue()
s.enqueue("1")
s.enqueue("2")
s.enqueue("3")
print(s.dequeue())
print(s.first())
            