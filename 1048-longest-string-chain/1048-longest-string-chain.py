class Solution(object):
    def ispred(self, p, c):
        if len(c) - len(p) != 1:
            return False

        i = 0
        j = 0

        while i < len(p) and j < len(c):
            if p[i] == c[j]:
                i += 1
            j += 1

        return i == len(p)

    def longestStrChain(self, words):
        words.sort(key=len)
        n = len(words)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if self.ispred(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)