from LinkedQueue import LinkedQueue
from TreeNode import TreeNode

class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def maketree(self, e, left, right):
        self.root = TreeNode(e, left.root, right.root)
        left.root = None
        right.root = None

    def levelorder(self):
        q = LinkedQueue()
        root_node = self.root
        print(root_node.data, end='--')
        q.enqueue(root_node)

        while not q.is_empty():
            node = q.dequeue()
            if node.left:
                print(node.left.data, end='--')
                q.enqueue(node.left)
            if node.right:
                print(node.right.data, end='--')
                q.enqueue(node.right)

    def inorder(self, root_node):
        if root_node:
            self.inorder(root_node.left)
            print(root_node.data, end='--')
            self.inorder(root_node.right)

    def preorder(self, root_node):
        if root_node:
            print(root_node.data, end='--')
            self.preorder(root_node.left)
            self.preorder(root_node.right)

    def postorder(self, root_node):
        if root_node:
            self.postorder(root_node.left)
            self.postorder(root_node.right)
            print(root_node.data, end='--')

################################################

a = BinaryTree()
x = BinaryTree()
y = BinaryTree()
z = BinaryTree()            
r = BinaryTree()
s = BinaryTree()
t = BinaryTree()

x.maketree(40, a, a)
y.maketree(60, a, a)
z.maketree(20, x, a)
r.maketree(50, a, y)
s.maketree(30, r, a)
t.maketree(10, z, s)

t.levelorder()
print()
t.preorder(t.root)
print()
t.inorder(t.root)
print()
t.postorder(t.root)
print()