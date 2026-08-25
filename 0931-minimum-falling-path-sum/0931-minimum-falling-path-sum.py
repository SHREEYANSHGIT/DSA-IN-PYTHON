class Solution(object):
    

    def find(self, i, j, matrix,dp):
        
        # Base case: reached last row
        if j < 0 or j >= len(matrix[0]):
            return float("inf")
        if i == len(matrix) - 1:
            return matrix[i][j]
        if dp[i][j] != "x":
            return dp[i][j]

        left = self.find(i + 1, j - 1, matrix,dp)
        down = self.find(i + 1, j, matrix,dp)
        right = self.find(i + 1, j + 1, matrix,dp)
        dp[i][j] = matrix[i][j] + min(left, right,down)
        return dp[i][j] 

    def minFallingPathSum(self, matrix):
        n = len(matrix[0])
        m = len(matrix)
        dp = [["x"] * n for _ in range(n)]
        dp[-1] = matrix[-1][:]
        result = float("inf")
        for j in range(n):
            ans = self.find(0, j, matrix,dp)
            if ans < result :
                result = ans

        return result
        
        
        