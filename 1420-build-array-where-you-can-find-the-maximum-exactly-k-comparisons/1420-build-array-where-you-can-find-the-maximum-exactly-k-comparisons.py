class Solution(object):
    def find(self, idx, sc, mi, n, m, k, dp):
        if sc > k:
            return 0

        if idx == n:
            return 1 if sc == k else 0

        if dp[idx][sc][mi] != -1:
            return dp[idx][sc][mi]

        result = 0

        for i in range(1, m + 1):
            if i > mi:
                result += self.find(idx+1, sc+1, i, n, m, k, dp)
            else:
                result += self.find(idx+1, sc, mi, n, m, k, dp)

            result %= self.mod

        dp[idx][sc][mi] = result
        return result

    def numOfArrays(self, n, m, k):
        self.mod = 10**9 + 7

        dp = [[[-1 for _ in range(m+1)]
               for _ in range(k+1)]
              for _ in range(n+1)]

        return self.find(0, 0, 0, n, m, k, dp)