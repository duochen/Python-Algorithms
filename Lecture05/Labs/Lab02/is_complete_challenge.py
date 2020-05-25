from collections import deque

# Data structure to store a Binary Tree node
class Node:
    def __init__(self, key=None, left=None, right=None):

        self.key = key
        self.left = left
        self.right = right

# Function to check if given Binary Tree is Complete or not
def isComplete(root):
    pass

if __name__ == '__main__':

    """ Construct below tree
              1
           /     \
          2       3
         / \     / \
        4   5   6   7
    """

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    if isComplete(root):
        print("Given Binary Tree is a Complete Binary Tree")
    else:
        print("Given Binary Tree is not a Complete Binary Tree")
