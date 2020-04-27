class EmptyQueueError(Exception):
    pass

class ArrayQueue:
    def __init__(self):
        self.data = []
        self.size = 0
        self.front = 0

    def len(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def enqueue(self, e):
        self.data.append(e)
        self.size = self.size + 1

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError('Queue is empty')
        value = self.data[self.front]
        self.data[self.front] = None
        self.front = self.front + 1
        self.size = self.size - 1
        return value

    def first(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")
        return self.data[self.front]

########################################################

q = ArrayQueue()
q.enqueue(10)
q.enqueue(20)
print('Queue: ', q.data)
print('Length: ', q.len())
print('Dequeue: ', q.dequeue())
print('Queue: ', q.data)
q.enqueue(30)
q.enqueue(40)
print('Queue: ', q.data)
print('Dequeue: ', q.dequeue())
print('Queue: ', q.data)