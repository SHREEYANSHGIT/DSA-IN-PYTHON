class Solution(object):
    def find(self,i,cost,dp):
        if i < 0:
            return 0
        
        if dp[i] != -1:
            return dp[i]
        
        right = self.find(i-2,cost,dp)
        left = self.find(i-1,cost,dp)

        dp[i] = cost[i] + min(right,left)

        return dp[i]
    def minCostClimbingStairs(self, cost):
        cost.append(0)
        n = len(cost)
        dp = [-1]*(n+1)
        return self.find(n-1,cost,dp)
        