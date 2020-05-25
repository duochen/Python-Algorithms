from collections import deque

# Data structure to store a Binary Tree node
class Node:
    def __init__(self, key=None, left=None, right=None):

        self.key = key
        self.left = left
        self.right = right

# Function to check if given Binary Tree is Complete or not
def isComplete(root):

    # return if tree is empty
    if root is None:
        return False

    # create an empty queue and enqueue root node
    queue = deque()
    queue.append(root)

    # flag to mark end of full nodes
    flag = False

    # run till queue is not empty
    while queue:

        # pop front node from the queue
        front = queue.popleft()

        # if we have encountered a non-full node before and current node
        # is not a leaf, tree cannot be complete tree
        if flag and (front.left or front.right):
            return False

        # if left child is empty & right child exists, tree cannot be complete
        if front.left is None and front.right:
            return False

        # if left child exists, enqueue it
        if front.left:
            queue.append(front.left)

        # if current node is a non-full node, set flag to True
        else:
            flag = True

        # if right child exists, enqueue it
        if front.right:
            queue.append(front.right)

        # if current node is a non-full node, set flag to True
        else:
            flag = True

    return True


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
