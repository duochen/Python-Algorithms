class ArrayStack:
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def empty(self):
        return self.size() == 0

    def push(self, e):
        self.data.append(e)

    def pop(self):
        if self.empty():
            raise ValueError('Stack is empty')
        return self.data.pop()

    def top(self):
        if self.empty():
            raise ValueError('Stack is empty')
        return self.data[-1]

s = ArrayStack()
s.push(10)
s.push(20)
print('Stack: ', s.data)
print('Length:', s.size())
print('Is stack empty:', s.empty())
print('Popped: ', s.pop())
print('Stack: ', s.data)
print("Stack top: ", s.top())
print('Popped: ', s.pop())
print('Stack: ', s.data)
print("Stack top: ", s.top())
