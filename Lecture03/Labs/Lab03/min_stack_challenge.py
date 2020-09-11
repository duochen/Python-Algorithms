class MinStack:
    def __init__(self):
        pass

    def push(self, x):
        pass

    def pop(self):
        pass

    def top(self): 
        pass

    def getMin(self):
        pass

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())   # return -3
print(minStack.pop())      # return (-3, -3)
print(minStack.top())      # return 0
print(minStack.getMin())   # return -2