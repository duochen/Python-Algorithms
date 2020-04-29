class Node:
    def __init__(self, element=None):
        self.element = element
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        node = self.head
        while node is not None:
            print(node.element)
            node = node.next

    def add_first(self, newdata):
        new_node = Node(newdata)
        new_node.next = self.head
        self.head = new_node

##########################################

list1 = LinkedList()
list1.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
list1.head.next = e2
e2.next = e3
list1.add_first("Sun")
list1.display()