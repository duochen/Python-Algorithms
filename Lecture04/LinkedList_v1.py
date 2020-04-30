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

##########################################

list1 = LinkedList()
list1.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
list1.head.next = e2
e2.next = e3
list1.display()