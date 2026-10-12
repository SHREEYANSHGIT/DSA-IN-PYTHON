class Solution(object):
    def find(self, i, k, n, tsum, path, ans, x):
        if tsum == n and x == k:
            ans.append(path[:])
            return

        if i > 9 or tsum > n or x >= k:
            return

        path.append(i)
        self.find(i + 1, k, n, tsum + i, path, ans, x + 1)
        path.pop()

        self.find(i + 1, k, n, tsum, path, ans, x)

    def combinationSum3(self, k, n):
        ans = []
        self.find(1, k, n, 0, [], ans, 0)
        return ans