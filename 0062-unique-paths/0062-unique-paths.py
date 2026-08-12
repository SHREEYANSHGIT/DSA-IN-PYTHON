class Solution(object):

    def dfs(self,i,j,m,n ,dp):
        if i == (m - 1) and j == (n-1):
            return 1 

        if dp[i][j]!=-1:
           return dp[i][j]

        right = 0
        down = 0

        if (i+1) < m:
            right = self.dfs( i+1 , j , m , n , dp)
        if (j+1) < n :
            down = self.dfs( i , j+1 , m , n , dp)

        dp[i][j] = right + down

        return dp[i][j]

        
    def uniquePaths(self, m, n):
        dp = [[-1 for _ in range(n)]for _ in range(m)]

        return self.dfs(0, 0, m, n, dp)