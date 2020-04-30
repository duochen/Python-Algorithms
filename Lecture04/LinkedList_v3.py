class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next

    def add_first(self, newdata):
        new_node = Node(newdata)
        new_node.next = self.head
        self.head = new_node

    def add_last(self, newdata):
        new_node = Node(newdata)
        if self.head is None:
            self.head = new_node
            return
        node = self.head
        while (node.next):
            node = node.next
        node.next = new_node

##########################################

list1 = LinkedList()
list1.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
list1.head.next = e2
e2.next = e3
list1.add_last("Thu")
list1.display()