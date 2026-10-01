class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        n = len(text1)
        m = len(text2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):

                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]

                else:
                    left = dp[i + 1][j]
                    right = dp[i][j + 1]

                    dp[i][j] = max(left, right)

        return dp[0][0]