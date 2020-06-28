from nose.tools import assert_equal
from MyLinkedList import MyLinkedList
from LinkedList import Node

class TestRemoveDupes:
    def test_remove_dupes(self, linked_list):
        linked_list.remove_dupes()
        assert_equal(linked_list.get_all_data(), [])

        linked_list.insert_to_front(2)
        linked_list.remove_dupes()
        assert_equal(linked_list.get_all_data(), [2])

        linked_list.insert_to_front(1)
        linked_list.insert_to_front(1)
        linked_list.insert_to_front(3)
        linked_list.insert_to_front(2)
        linked_list.insert_to_front(3)
        linked_list.insert_to_front(1)
        linked_list.insert_to_front(1)
        linked_list.remove_dupes()
        assert_equal(linked_list.get_all_data(), [1, 3, 2])

    def test_palindrome(self):
        linked_list = MyLinkedList()
        assert_equal(linked_list.is_palindrome(), False)

        print('Test: Single element list')
        head = Node(1)
        linked_list = MyLinkedList(head)
        assert_equal(linked_list.is_palindrome(), False)

        print('Test: Two element list, not a palindrome')
        linked_list.append(2)
        assert_equal(linked_list.is_palindrome(), False)

        print('Test: General case: Palindrome with even length')
        head = Node('a')
        linked_list = MyLinkedList(head)
        linked_list.append('b')
        linked_list.append('b')
        linked_list.append('a')
        assert_equal(linked_list.is_palindrome(), True)

        print('Test: General case: Palindrome with odd length')
        head = Node(1)
        linked_list = MyLinkedList(head)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(2)
        linked_list.append(1)
        assert_equal(linked_list.is_palindrome(), True)

    def test_delete_node(self):
        print('Test: Empty list, null node to delete')
        linked_list = MyLinkedList(None)
        linked_list.delete_node(None)
        assert_equal(linked_list.get_all_data(), [])

        print('Test: One node')
        head = Node(2)
        linked_list = MyLinkedList(head)
        linked_list.delete_node(head)
        assert_equal(linked_list.get_all_data(), [None])

        print('Test: Multiple nodes')
        linked_list = MyLinkedList(None)
        node0 = linked_list.insert_to_front(2)
        node1 = linked_list.insert_to_front(3)
        node2 = linked_list.insert_to_front(4)
        node3 = linked_list.insert_to_front(1)
        linked_list.delete_node(node1)
        assert_equal(linked_list.get_all_data(), [1, 4, 2])

        print('Test: Multiple nodes, delete last element')
        linked_list = MyLinkedList(None)
        node0 = linked_list.insert_to_front(2)
        node1 = linked_list.insert_to_front(3)
        node2 = linked_list.insert_to_front(4)
        node3 = linked_list.insert_to_front(1)
        linked_list.delete_node(node0)
        assert_equal(linked_list.get_all_data(), [1, 4, 3, None])

        print('Success: test_delete_node')



def main():
    test = TestRemoveDupes()
    test.test_delete_node()

if __name__ == '__main__':
    main()
