
class Solution(object):
    def numDecodings(self, s):
        n = len(s)
        dp = [0] * (n + 1)

        dp[0] = 1

        if s[0] == "0":
            return 0

        dp[1] = 1

        for i in range(2, n + 1):
            last = dp[i - 1]
            slast = dp[i - 2]

            if s[i - 1] != "0":
                dp[i] += last

            if 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += slast

        return dp[n]
