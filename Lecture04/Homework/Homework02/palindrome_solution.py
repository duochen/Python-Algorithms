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
        if self.head is None or self.head.next is None:
            return False
        curr = self.head
        reversed_list = MyLinkedList()
        length = 0

        # Reverse the linked list
        while curr is not None:
            reversed_list.insert_to_front(curr.data)
            length += 1
            curr = curr.next

        # Compare the reversed list with the original list
        # Only need to compare the first half
        iterations = length // 2
        curr = self.head
        curr_reversed = reversed_list.head
        for _ in range(iterations):
            if curr.data != curr_reversed.data:
                return False
            curr = curr.next
            curr_reversed = curr_reversed.next
        return True

head = Node(1)
linked_list = MyLinkedList(head)
linked_list.append(2)
linked_list.append(3)
linked_list.append(2)
linked_list.append(1)
print(linked_list.is_palindrome()==True)

head = Node('a')
linked_list = MyLinkedList(head)
linked_list.append('b')
linked_list.append('b')
linked_list.append('a')
print(linked_list.is_palindrome(), True)