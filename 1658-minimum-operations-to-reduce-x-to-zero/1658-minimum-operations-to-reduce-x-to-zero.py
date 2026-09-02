class Solution(object):
    def minOperations(self, nums, x):
        total = sum(nums)
        target = total - x

        if target < 0:
            return -1

        if target == 0:
            return len(nums)

        l = 0
        r = 0
        curr_sum = 0
        maxi = -1

        while r < len(nums) or curr_sum > target:

            if curr_sum > target:
                curr_sum -= nums[l]
                l += 1

            else:
                curr_sum += nums[r]
                r += 1

            if curr_sum == target:
                maxi = max(maxi, r - l)

        return -1 if maxi == -1 else len(nums) - maxi