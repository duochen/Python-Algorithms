from collections import deque

# Data structure to store a Binary Tree node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# Function to check if given node is a leaf node or not
def isLeaf(node):
    pass

# Recursive function to find paths from root node to every leaf node
def printRootToLeafPaths(node, path):
    pass

# Main function to print paths from root node to every leaf node
def printRootToLeafPath(node):
    pass


if __name__ == '__main__':

    """ Construct below tree
              1
            /   \
           /     \
          2       3
         / \     / \
        4   5   6   7
               /     \
              8       9
    """

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.left = Node(8)
    root.right.right.right = Node(9)

    # print all root to leaf paths
    printRootToLeafPath(root)
