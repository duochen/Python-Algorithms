class Node:
    
    def __init__(self, data, next=None):
        self.next = next
        self.data = data

class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def insert_to_front(self, data):
        if data is None:
            return None
        node = Node(data, self.head)
        self.head = node
        return node

    def get_all_data(self):
        data = []
        curr_node = self.head
        while curr_node is not None:
            data.append(curr_node.data)
            curr_node = curr_node.next
        return data

class MyLinkedList(LinkedList):
    
    def remove_dupes(self):
        pass
    
linked_list = MyLinkedList()
linked_list.insert_to_front(1)
linked_list.insert_to_front(1)
linked_list.insert_to_front(3)
linked_list.insert_to_front(2)
linked_list.insert_to_front(3)
linked_list.insert_to_front(1)
linked_list.insert_to_front(1)
linked_list.remove_dupes()
print(linked_list.get_all_data() == [1, 3, 2])