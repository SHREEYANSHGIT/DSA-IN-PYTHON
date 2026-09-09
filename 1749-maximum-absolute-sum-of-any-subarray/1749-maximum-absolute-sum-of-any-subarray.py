class Solution(object):
    def maxAbsoluteSum(self, nums):
        mini = float("inf")
        maxi = float("-inf")
        c1 = 0
        c2 = 0
        n = len(nums)

        for i in range(n):
            c1 += nums[i]
            maxi = max(maxi,c1)

            c2 += nums[i]
            mini = min(mini , c2)
            
            if c2 > 0 :
                c2 = 0

            if c1 < 0:
                c1 = 0

        return max(maxi , abs(mini))

