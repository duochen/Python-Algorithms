# https://www.geeksforgeeks.org/find-k-th-smallest-element-in-bst-order-statistics-in-bst/
# A simple inorder traversal based Python3
# program to find k-th smallest element
# in a BST.
 
# A BST node
class Node:
     
    def __init__(self, key):
         
        self.data = key
        self.left = None
        self.right = None

def kthSmallest(root):
     
    global k
     
    # Base case
    if (root == None):
        return None
 
    # Search in left subtree
    left = kthSmallest(root.left)
 
    # If k'th smallest is found in
    # left subtree, return it
    if (left != None):
        return left
         
    # If current element is k'th
    # smallest, return it
    k -= 1
    if (k == 0):
        return root
 
    # Else search in right subtree
    return kthSmallest(root.right)
 
# Function to find k'th largest element in BST
def printKthSmallest(root):
     
    # Maintain index to count number
    # of nodes processed so far
    res = kthSmallest(root)
     
    if (res == None):
        print("There are less than k nodes in the BST")
    else:
        print("K-th Smallest Element is ", res.data)
 
# Driver code
if __name__ == '__main__':
    root = Node(8)  
    root.left = Node(5)  
    root.right = Node(14) 
    root.left.left = Node(4)  
    root.left.right = Node(6) 
    root.right.right = Node(24) 
    root.right.right.left = Node(22)

    k = 2
    printKthSmallest(root)

    k = 3
    printKthSmallest(root)