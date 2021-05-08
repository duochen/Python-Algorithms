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

    def append(self, data):
        if data is None:
            return None
        node = Node(data)
        if self.head is None:
            self.head = node
            return node
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = node
        return node

    def get_all_data(self):
        data = []
        curr_node = self.head
        while curr_node is not None:
            data.append(curr_node.data)
            curr_node = curr_node.next
        return data

class MyLinkedList(LinkedList):
    
    def is_palindrome(self):
        # TODO: Implement me
        pass

head = Node(1)
linked_list = MyLinkedList(head)
linked_list.append(2)
linked_list.append(3)
linked_list.append(2)
linked_list.append(1)
print(linked_list.is_palindrome()==True)