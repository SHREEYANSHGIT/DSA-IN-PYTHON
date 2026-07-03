class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        totalsum = sum(nums)
        left = 0
        for i in range (n):
            if left == totalsum - left - nums[i]:
                return i
            left += nums[i]

        return -1