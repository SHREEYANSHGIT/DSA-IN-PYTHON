class Solution(object):
    def singleNumber(self, nums):
        n = len(nums)
        ans = 0
        for i in range(n):
            ans= ans^nums[i]
        return ans
        

        