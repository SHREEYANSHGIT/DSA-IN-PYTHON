class Solution(object):
    def findDuplicates(self, nums):
        n = len(nums)
        ans = []
        for i in range(n):
            x = abs(nums[i])
            if nums[x-1] < 0:
                ans.append(x)
            else:
                y = nums[x-1]
                nums[x-1] = -y
        return ans
        