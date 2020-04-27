# Implementation of the simple stack ADT using list
class SimpleArrayStack:
    def __init__(self, limit=10):
        self.data = []
        self.limit = limit

    def size(self):
        return len(self.data)

    def empty(self):
        return self.size() <= 0

    def push(self, item):
        if len(self.data) >= self.limit:
            print('Stack Overflow!')
        else:
            self.data.append(item)

    def pop(self):
        if len(self.data) <= 0:
            print('Stack Underflow!')
            return 0
        else:
            return self.data.pop()

    def top(self):
        if len(self.data) <= 0:
            print('Stack Underflow!')
            return 0
        else:
            return self.data[-1]

########################################################

s = SimpleArrayStack(5)
s.push("1")
s.push("21")
s.push("14")
s.push("31")
s.push("19")
s.push("3")
s.push("99")
s.push("9")
print(s.data)
print(s.top())
print(s.pop())
print(s.data)
print(s.top())
print(s.pop())
print(s.data)
