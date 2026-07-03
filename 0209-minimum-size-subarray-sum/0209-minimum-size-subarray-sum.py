class Solution(object):
    def minSubArrayLen(self, target, nums):
        n = len(nums)
        l = 0
        r = 0
        
        sum_target = 0
        mini = float("inf")

        for i in range(n):
            if sum_target < target:
                sum_target = sum_target + nums[r]
                r = r+1
            
            while sum_target >= target:
                mini = min(mini , r-l)
                sum_target = sum_target - nums[l]
                l = l+1
            

            
        return 0 if mini == float("inf") else mini  

            



