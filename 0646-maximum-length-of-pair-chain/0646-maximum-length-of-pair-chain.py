class Solution(object):
    def findLongestChain(self, pairs):
        pairs = sorted(pairs)
        n = len(pairs)
        dp = [1] * n
        maxi = 1
        for i in range(1,n):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i] , dp[j] +1)
                    maxi = max(dp[i] , maxi)
        return maxi

