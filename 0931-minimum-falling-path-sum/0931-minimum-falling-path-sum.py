class Solution(object):

    def minFallingPathSum(self, matrix):

        n = len(matrix)

        curr = ["x"]*n

        # Base case: last row
        prev = matrix[n-1][:]

        # Bottom -> top
        for i in range(n-2, -1, -1):

            for j in range(n):

                # Down
                down = prev[j]

                # Left-down
                if j > 0:
                    left = prev[j-1]
                else:
                    left = float("inf")

                # Right-down
                if j < n-1:
                    right = prev[j+1]
                else:
                    right = float("inf")
                curr[j] = matrix[i][j] + min(left, down, right)
            prev = curr
            curr = ["x"]*n 

        return min(prev)