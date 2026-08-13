class Solution(object):
    def dfs(self, i, j, rows, cols, obstacleGrid,dp):

        # Obstacle
        if obstacleGrid[i][j] == 1:
            return 0

        # Destination
        if i == rows - 1 and j == cols - 1:
            return 1
        
        # Already calculated
        if dp[i][j] != -1:
            return dp[i][j]

        r = 0
        d = 0

        # Move down
        if i + 1 < rows:
            d = self.dfs(i + 1, j, rows, cols, obstacleGrid,dp)

        # Move right
        if j + 1 < cols:
            r = self.dfs(i, j + 1, rows, cols, obstacleGrid,dp)

        dp[i][j] = r+d
        return dp[i][j] 


    def uniquePathsWithObstacles(self, obstacleGrid):
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        dp = [[-1 for _ in range(cols)]for _ in range(rows)]
        
        return self.dfs(0, 0, rows, cols, obstacleGrid,dp)