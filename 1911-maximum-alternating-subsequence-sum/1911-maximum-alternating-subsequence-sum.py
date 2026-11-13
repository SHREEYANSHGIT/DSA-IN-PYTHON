class Solution(object):
    def find(self,i,nums,flag,dp):
        if i >= len(nums):
            return 0
        if dp[i][flag] != -1:
            return dp[i][flag]
        skip = self.find(i+1 ,nums , flag,dp)
        val = nums[i]

        if flag == False:
            val = -val

        x = not flag
        take = val + self.find(i+1 ,nums , x,dp)

        dp[i][flag] = max(take,skip)
        return dp[i][flag]
        
    def maxAlternatingSum(self, nums):
        n = len(nums)
        dp = [[-1 for _ in range(2)] for _ in range(n)]
        return self.find(0 ,nums , True,dp)