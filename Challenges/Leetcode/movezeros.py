class Solution:
    def moveZeroes(self, nums):
        j = 0
        for num in nums:
            if(num != 0):
                nums[j] = num
                j += 1

        for x in range(j, len(nums)):
            nums[x] = 0

input = [0,1,0,3,12]
s = Solution()
s.moveZeroes(input)
print(input)