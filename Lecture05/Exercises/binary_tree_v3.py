class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, newdata):
        if self.data:
            if newdata < self.data:
                if self.left is None:
                    self.left = Node(newdata)
                else:
                    self.left.insert(newdata)
            elif newdata > self.data:
                if self.right is None:
                    self.right = Node(newdata)
                else:
                    self.right.insert(newdata)
            else:
                self.data = newdata

    def display(self):
        if self.left:
            self.left.display()
        print(self.data)
        if self.right:
            self.right.display()

#######################################

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.display()