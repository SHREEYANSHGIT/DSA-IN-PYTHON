class Solution(object):
        
    def maxAlternatingSum(self, nums):
        n = len(nums)
        dp = [[0 for _ in range(2)] for _ in range(n+1)]
        lastodd = 0
        lasteven = 0 
        neweven = 0
        newodd = 0


        for i in range(1,n+1):
            neweven = max(lastodd - nums[i-1] , neweven)
            newodd = max(lasteven + nums[i-1] , newodd)
            lasteven = neweven 
            lastodd = newodd 


        return max(newodd, neweven)