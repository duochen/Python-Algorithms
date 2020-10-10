class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def level_order(queue):
        if len(queue) == 0:
            return

        node = queue[0]
        queue.pop(0)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

        print(node.data)
        level_order(queue)
"""
Given the following input tree:
          1
        /   \
       2     3
      /     / \
     4      5  6

The output is:
1
2 3
4 5 6

or 
1 
2 
3 
4 
5 
6
"""


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
queue = list()
queue.append(root)
level_order(queue)