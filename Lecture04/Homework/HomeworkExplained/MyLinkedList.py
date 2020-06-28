from LinkedList import LinkedList

class MyLinkedList(LinkedList):
    def delete_node(self, node):
        if node is None:
            return
        if node.next is None:
            node.data = None
        else:
            node.data = node.next.data
            node.next = node.next.next


    def remove_dupes(self):
        if self.head is None:
            return
        seen_data = set()
        node = self.head
        while node is not None:
            if node.data not in seen_data:
                seen_data.add(node.data)
                prev = node
                node = node.next
            else:  # Found duplicate
                prev.next = node.next
                node = node.next

    def is_palindrome(self):
        if self.head is None or self.head.next is None:
            return False  

        reversed_list = MyLinkedList()
        curr = self.head
        length = 0

        # Reverse the linked list
        while curr is not None:
            reversed_list.insert_to_front(curr.data)
            length += 1
            curr = curr.next

        # Compare the reversed list with the original list
        # Only need to compare the first half
        iterations = int(length / 2)
        curr = self.head
        curr_reversed = reversed_list.head
        for _ in range(iterations):
            if curr.data != curr_reversed.data:
                return False
            curr = curr.next
            curr_reversed = curr_reversed.next
        return True


        