class Solution(object):
    def minOperations(self, nums, x):
        target = sum(nums) - x

        if target < 0:
            return -1

        l = 0
        curr_sum = 0
        maxi = -1

        for r in range(len(nums)):
            curr_sum += nums[r]

            while curr_sum > target:
                curr_sum -= nums[l]
                l += 1

            if curr_sum == target:
                maxi = max(maxi, r - l + 1)

        if target == 0:
            return len(nums)

        return -1 if maxi == -1 else len(nums) - maxi