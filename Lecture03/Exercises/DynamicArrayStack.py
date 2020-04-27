# Implementation of the dynamic stack ADT using list
class DynamicArrayStack:
    def __init__(self, limit=10):
        self.data = limit*[None]
        self.limit = limit

    def resize(self):
        newStk = list(self.data)
        self.limit = 2*self.limit
        self.data = newStk

    def size(self):
        return len(self.data)

    def empty(self):
        return self.size() <= 0

    def push(self, item):
        if len(self.data) >= self.limit:
            self.resize()
        self.data.append(item)
        print('Stack after push', self.data)

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

s = DynamicArrayStack(5)
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
