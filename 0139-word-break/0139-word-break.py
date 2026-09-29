class Solution(object):

    def find(self, i, s, wordDict, dp):

        if i == len(s):
            return True

        # Already calculated
        if i in dp:
            return dp[i]

        for j in range(i + 1, len(s) + 1):
            a = s[i:j]

            if a in wordDict:
                if self.find(j, s, wordDict, dp):
                    dp[i] = True
                    return True

        dp[i] = False
        return False

    def wordBreak(self, s, wordDict):
        dp = {}
        return self.find(0, s, wordDict, dp)