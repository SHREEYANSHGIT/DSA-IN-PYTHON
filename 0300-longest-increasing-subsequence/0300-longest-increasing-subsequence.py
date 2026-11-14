class Solution(object):
    def find(self, i, p, nums, dp):
        if i >= len(nums):
            return 0

        if p != -1 and dp[i][p] != -1:
            return dp[i][p]

        take = 0
        if p == -1 or nums[p] < nums[i]:
            take = 1 + self.find(i+1, i, nums, dp)

        skip = self.find(i+1, p, nums, dp)
        if p!= -1:
            dp[i][p] = max(take, skip)
        return max(take, skip)

    def lengthOfLIS(self, nums):
        n = len(nums)
        dp = [1] *(n)

        for i in range(1,n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i] <= dp[j]:
                        dp[i] += 1 
        return max(dp)
            
        