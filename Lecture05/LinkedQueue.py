from Node import Node
from EmptyLinkedQueueError import EmptyLinkedQueueError

class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def len(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def enqueue(self, e):
        new_node = Node(e, None)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size = self.size + 1

    def dequeue(self):
        if self.is_empty():
            raise EmptyLinkedQueueError('Queue is empty')
        value = self.head.data
        self.head = self.head.next
        self.size = self.size - 1
        if self.is_empty():
            self.tail = None
        return value

    def first(self):
        if self.is_empty():
            raise EmptyLinkedQueueError('Queue is empty')
        return self.head.data

    def display(self):
        head_node = self.head
        while head_node:
            print(head_node.data, end='-->')
            head_node = head_node.next
        print()

###########################################            

q = LinkedQueue()
q.enqueue(10)
q.enqueue(20)
q.display()
print('Length: ', q.len())
print('Dequeue: ', q.dequeue())
q.display()
q.enqueue(30)
q.enqueue(40)
q.display()
print('First Element: ', q.first())
q.display()
print('Dequeue: ', q.dequeue())
q.display()
