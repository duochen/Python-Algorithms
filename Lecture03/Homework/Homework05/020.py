class Solution:
    def isEqual(self, c1, c2):
        if (c1 == '(' and c2 == ')'):
            return True
        if (c1 == '[' and c2 == ']'):
            return True
        if (c1 == '{' and c2 == '}'):
            return True

        return False

    def isValid(self, s):
        st = []

        for character in s:
            if (len(st) != 0):
                li = st[-1]
                if (self.isEqual(li, character)):
                    st.pop()
                    continue
            st.append(character)

        return len(st) == 0

s = Solution()
print(s.isValid("()[]{}"))
print(s.isValid("([)])"))