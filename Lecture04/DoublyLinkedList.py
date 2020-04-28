from Node import DoubleNode
from EmptyLinkedListError import EmptyLinkedListError

class DoublyLinkedList:
    def __init__(self):
        self.head = DoubleNode(None,None,None)
        self.tail = DoubleNode(None,None,None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def len(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def add_first(self, e):
        new_node = DoubleNode(e,None,None)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node
        self.size += 1

    def add_last(self, e):
        new_node = DoubleNode(e,None,None)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node
        self.size += 1

    def add_any(self, e, pos):
        new_node = DoubleNode(e,None,None)
        head_node = self.head
        i = 1
        while i < pos:
            head_node = head_node.next
            i += 1
        new_node.next = head_node.next
        head_node.next = new_node
        head_node.next.prev = new_node
        new_node.prev = head_node
        self.size += 1

    def remove_first(self):
        if self.is_empty():
            raise EmptyLinkedListError('Linked List Empty')
        value = self.head.element
        self.head = self.head.next
        self.head.prev = None
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return value

    def remove_last(self):
        if self.is_empty():
            raise EmptyLinkedListError('Linked List Empty')
        head_node = self.head
        i = 0
        while i < self.len() - 2:
            head_node = head_node.next
            i += 1
        self.tail = head_node
        head_node = head_node.next
        value = head_node.element
        self.tail.next = None
        self.size -= 1
        return value

    def remove_any(self, pos):
        if self.is_empty():
            raise EmptyLinkedListError('Linked List Empty')
        head_node = self.head
        i = 1
        while i < pos-1:
            head_node = head_node.next
            i += 1
        head_node.next = head_node.next.next
        head_node.next.next.prev = head_node
        self.size -= 1

    def display(self):
        head_node = self.head
        while head_node:
            print(head_node.element, end='-->') 
            head_node = head_node.next
        print()

###############################################################################

l = DoublyLinkedList()
l.add_last(10)
l.add_last(20)
l.add_last(30)
l.add_last(40)        
l.display()
print('Deleted: ', l.remove_first())    
l.display()
l.add_first(60)
l.display()
print('Deleted: ', l.remove_last())
l.display()
l.add_any(90, 2)
l.display()
l.remove_any(2)
l.display()
