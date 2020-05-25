# Definition: Binary tree node.
class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def delete_Node(root, key):
    pass

def preOrder(node): 
    if not node: 
        return      
    print(node.val)
    preOrder(node.left) 
    preOrder(node.right)   
    
root = TreeNode(5)  
root.left = TreeNode(3)  
root.right = TreeNode(6) 
root.left.left = TreeNode(2)  
root.left.right = TreeNode(4) 
root.left.right.left = TreeNode(7)  
print("Original node:")
print(preOrder(root))
result = delete_Node(root, 4)
print("After deleting specified node:")
print(preOrder(result))