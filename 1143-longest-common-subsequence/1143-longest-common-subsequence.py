class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        n = len(text1)
        m = len(text2)

        dp = {}

        # Base cases
        for i in range(n + 1):
            dp[(i, m)] = 0

        for j in range(m + 1):
            dp[(n, j)] = 0

        # Bottom-up
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):

                if text1[i] == text2[j]:
                    dp[(i, j)] = 1 + dp[(i + 1, j + 1)]

                else:
                    left = dp[(i + 1, j)]
                    right = dp[(i, j + 1)]

                    dp[(i, j)] = max(left, right)

        return dp[(0, 0)]