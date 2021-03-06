class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def search(self, value):
        if value < self.data:
            if self.left is None:
                return str(value) + " Not Found"
            return self.left.search(value)
        elif value > self.data:
            if self.right is None:
                return str(value) + " Not Found"
            return self.right.search(value)
        else:
            print(str(self.data) + ' is found')

    def display(self):
        if self.left:
            self.left.display()
        print(self.data)
        if self.right:
            self.right.display()

##################################################################

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.display()
print(root.search(7))
print(root.search(14))