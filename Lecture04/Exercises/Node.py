class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class DoubleNode:
    slots = 'data', 'prev', 'next'
    
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next
