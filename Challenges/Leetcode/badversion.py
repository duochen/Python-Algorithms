class Solution:
    def  isBadVersion(self, version):
        if version >= 3:
            return True
        else:
            return False

    def firstBadVersion(self, n):
        left = 1
        right = n

        while(left < right):
            mid = left+(right-left)//2
            if not self.isBadVersion(mid):
                left = mid+1
            else:
                right = mid
        return left

s = Solution()
result = s.firstBadVersion(7)
print(result)