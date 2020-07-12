class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def level_order(queue):
    pass

queue = list()
root = Node(1)
queue.append(root)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)

level_order(queue)