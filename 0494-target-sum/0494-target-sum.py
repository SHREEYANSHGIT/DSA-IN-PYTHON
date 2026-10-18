
class Solution(object):
    def find(self, i, nums, target, n, s, dp):
        if i >= n:
            if target == s:
                return 1
            return 0

        if (i, s) in dp:
            return dp[(i, s)]

        pick = self.find(i + 1, nums, target, n, s - nums[i], dp)
        npick = self.find(i + 1, nums, target, n, s + nums[i], dp)

        dp[(i, s)] = pick + npick
        return dp[(i, s)]

    def findTargetSumWays(self, nums, target):
        if abs(target) > sum(nums):
            return 0

        n = len(nums)
        dp = {}
        return self.find(0, nums, target, n, 0, dp)
