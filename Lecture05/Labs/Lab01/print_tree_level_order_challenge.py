from collections import deque

class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val =  val

def levelOrderPrint(tree):
    pass

##############################################

root =  Node(1)
root.left = Node(2)    
root.left.left = Node(4)
root.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(6)

levelOrderPrint(root)
