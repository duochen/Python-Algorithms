class Queue:
    def __init__(self):
        self.data = list()

    def enqueue(self, e):
        if e not in self.data:
            self.data.insert(0, e)
            return True
        else:
            return False
    
    def size(self):
        return len(self.data)

###########################################
q = Queue()
q.enqueue("Mon")
q.enqueue("Tue")
q.enqueue("Wed")
print(q.size())