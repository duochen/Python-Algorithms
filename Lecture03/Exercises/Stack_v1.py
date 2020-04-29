class Stack:
    def __init__(self):
        self.data = []

    def add(self, item):
        if item not in self.data:
            self.data.append(item)
            return True
        else:
            return False

    def peek(self):
        return self.data[-1]

##########################################
s = Stack()
s.add("Mon")
s.add("Tue")
s.peek()
print(s.peek())
s.add("Wed")
s.add("Thu")
print(s.peek())