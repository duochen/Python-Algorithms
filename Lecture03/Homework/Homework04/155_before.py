# https://leetcode.com/problems/min-stack/
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