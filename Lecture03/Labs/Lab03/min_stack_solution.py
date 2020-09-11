class MinStack:
    def __init__(self):
        self.st = []

    def push(self, x):
        curMin = self.getMin()
        if curMin == None or curMin > x:
            curMin = x
        self.st.append((x, curMin))

    def pop(self):
        return self.st.pop()

    def top(self): 
        return self.st[-1][0] if self.st else None

    def getMin(self):
        return self.st[-1][1] if self.st else None

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())   # return -3
print(minStack.pop())      # return (-3, -3)
print(minStack.top())      # return 0
print(minStack.getMin())   # return -2
