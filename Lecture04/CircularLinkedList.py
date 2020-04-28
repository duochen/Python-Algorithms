from Node import Node
from EmptyLinkedListError import EmptyLinkedListError

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def len(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0

    def add_first(self, e):
        newest = Node(e, None)
        if self.is_empty():
            newest.next = newest
            self.head = newest
            self.tail = newest
        else:
            self.tail.next = newest
            newest.next = self.head
        self.head = newest
        self.size += 1

    def add_last(self, e):
        