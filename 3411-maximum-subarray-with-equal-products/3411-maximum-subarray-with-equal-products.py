
class Solution(object):

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def maxLength(self, nums):
        n = len(nums)
        maxi = 0

        for i in range(n):
            p = 1
            g = 0
            lc = 1

            for j in range(i, n):
                x = nums[j]

                p *= x
                g = self.gcd(g, x)
                lc = (lc * x) // self.gcd(lc, x)

                if p == g * lc:
                    maxi = max(maxi, j - i + 1)

        return maxi
