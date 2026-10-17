
class Solution(object):
    def find(self, i, s, c, dp):
        if i == len(s):
            return 1

        if s[i] == '0':
            return 0

        if i in dp:
            return dp[i]

        c = 0

        for j in range(i, min(i + 2, len(s))):
            a = s[i:j+1]

            if 1 <= int(a) <= 26:
                c += self.find(j + 1, s, c, dp)

        dp[i] = c
        return c

    def numDecodings(self, s):
        dp = {}
        return self.find(0, s, 0, dp)
