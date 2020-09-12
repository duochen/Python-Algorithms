def isValid(s):
    pass

s = "()"
print(isValid(s))  # True
s = "()[]{}"
print(isValid(s))  # True
s = "(]"
print(isValid(s))  # False
s = "([)]"
print(isValid(s))  # False
s = "{[]}"
print(isValid(s))  # True