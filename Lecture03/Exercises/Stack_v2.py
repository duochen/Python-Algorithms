class Stack:
    def __init__(self):
        self.data = []

    def add(self, item):
        if item not in self.data:
            self.data.append(item)
            return True
        else:
            return False

    def remove(self):
        if len(self.data) <= 0:
            return ("No element in the Stack")
        else:
            return self.data.pop()

    def peek(self):
        return self.data[-1]

##########################################
s = Stack()
s.add("Mon")
s.add("Tue")
s.add("Wed")
s.add("Thu")
print(s.remove())
print(s.remove())