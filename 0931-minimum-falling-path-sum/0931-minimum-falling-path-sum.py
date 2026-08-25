class Solution(object):

    def minFallingPathSum(self, matrix):

        n = len(matrix)

        dp = [[0] * n for _ in range(n)]

        # Base case: last row
        dp[n-1] = matrix[n-1][:]

        # Bottom -> top
        for i in range(n-2, -1, -1):

            for j in range(n):

                # Down
                down = dp[i+1][j]

                # Left-down
                if j > 0:
                    left = dp[i+1][j-1]
                else:
                    left = float("inf")

                # Right-down
                if j < n-1:
                    right = dp[i+1][j+1]
                else:
                    right = float("inf")
                dp[i][j] = matrix[i][j] + min(left, down, right)
                ans = dp[i][j]

        return min(dp[0])