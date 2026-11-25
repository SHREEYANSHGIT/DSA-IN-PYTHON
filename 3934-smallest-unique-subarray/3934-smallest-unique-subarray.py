
class Solution(object):

    MOD = 10**9 + 7

    # Binary exponentiation
    def findPower(self, a, base):
        if base == 0:
            return 1

        half = self.findPower(a, base // 2)
        result = (half * half) % self.MOD

        if base % 2 == 1:
            result = (result * a) % self.MOD

        return result

    def check(self, nums, size, base):
        n = len(nums)

        h = 0
        mp = {}

        p = self.findPower(base, size - 1)

        i = 0
        j = 0

        while j < n:
            h = (h * base + nums[j]) % self.MOD

            if j - i + 1 < size:
                j += 1
            else:
                mp[h] = mp.get(h, 0) + 1

                h = (h - (p * nums[i]) % self.MOD + self.MOD) % self.MOD

                i += 1
                j += 1

        for val in mp.values():
            if val == 1:
                return True

        return False

    def smallestUniqueSubarray(self, nums):
        n = len(nums)

        base = max(nums) + 1

        l = 1
        r = n

        result = n

        while l <= r:
            mid = l + (r - l) // 2

            if self.check(nums, mid, base):
                result = mid
                r = mid - 1
            else:
                l = mid + 1

        return result
