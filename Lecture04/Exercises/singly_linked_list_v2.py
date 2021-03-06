class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class singly_linked_list:
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

##########################################

list1 = singly_linked_list()
list1.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
list1.head.next = e2
e2.next = e3
list1.add_first("Sun")
list1.display()