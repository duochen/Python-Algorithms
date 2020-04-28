class Node:
    slots = 'element', 'next'

    def __init__(self, element, next):
        self.element = element
        self.next = next

class DoubleNode:
    slots = 'element', 'prev', 'next'
    
    def __init__(self, element, prev, next):
        self.element = element
        self.prev = prev
        self.next = next
