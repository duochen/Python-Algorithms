# https://leetcode.com/problems/min-stack/
class MinStack:
    def __init__(self):
        self.st = []

    def push(self, x):
        curMin = self.getMin()
        if curMin == None or curMin > x:
            curMin = x
        self.st.append((x, curMin))

    def pop(self):
        self.st.pop()

    def top(self):
        if self.st:
            return self.st[-1][0]
        else:
            return None
         

    def getMin(self):
        if self.st:
            return self.st[-1][1]
        else:
            return None

"""
Input
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]
"""
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())    # return -3
minStack.pop()
print(minStack.top())       # return 0
print(minStack.getMin())    # return -2