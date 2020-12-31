class Node:
    def __init__(self, data, next=None):
        self.next = next
        self.data = data
        
class MyLinkedList:
    def __init__(self):
        self.head = None

    def add_first(self, data):
        if data is None:
            return None
        
        node = Node(data, self.head)
        self.head = node
        return node        

    def delete_node(self, node):
        if node is None:
            return
        if node.next is None:
            node.data = None
        else:
            node.data = node.next.data
            node.next = node.next.next

    def display(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next

list = MyLinkedList()
list.add_first(2)
list.add_first(3)
list.add_first(4)
list.add_first(1)
print("Before deletion")
list.display()
print("The node needs to be deleted: ", list.head.next.next.data)
list.delete_node(list.head.next.next)
print("After deletion")
list.display()

