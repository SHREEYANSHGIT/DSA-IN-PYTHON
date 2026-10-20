
class Solution(object):
    def find(self, n, dp):
        if n == 0:
            return 0

        if dp[n] != -1:
            return dp[n]

        ans = float("inf")

        for i in range(1, int(n**0.5) + 1):
            c = 1 + self.find(n - i**2, dp)
            ans = min(ans, c)

        dp[n] = ans
        return ans

    def numSquares(self, n):
        dp = [-1] * (n + 1)
        return self.find(n, dp)
