class Solution(object):
    def runningSum(self, nums):
        s = 0

        for i in range(len(nums)):
            s += nums[i]
            nums[i] = s
        
        return nums