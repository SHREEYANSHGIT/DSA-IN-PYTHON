class Solution(object):
    def find(self, i, short, m, n, dp):
        if i == len(short):
            return 0

        if dp[i][m][n] != -1:
            return dp[i][m][n]

        zeros, ones = short[i]

        pick = 0
        if zeros <= m and ones <= n:
            pick = 1 + self.find(
                i + 1, short, m - zeros, n - ones, dp
            )

        notpick = self.find(i + 1, short, m, n, dp)

        dp[i][m][n] = max(pick, notpick)
        return dp[i][m][n]

    def findMaxForm(self, strs, m, n):
        short = []

        for word in strs:
            zeros = word.count('0')
            ones = word.count('1')
            short.append([zeros, ones])

        k = len(strs)
        dp = [[[-1] * (n + 1) for _ in range(m + 1)]
              for _ in range(k)]

        return self.find(0, short, m, n, dp)