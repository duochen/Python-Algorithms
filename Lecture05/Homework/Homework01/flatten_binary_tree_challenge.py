class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val =  val

def flatten(root):
    pass

root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right = Node(5)  
root.right.right = Node(6)
flatten(root)
print(root.val)
while root.right is not None:
    print(root.right.val)
    root = root.right

