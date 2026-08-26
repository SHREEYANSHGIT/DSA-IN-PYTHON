class Solution(object):
    def findMin(self, nums):
        n = len(nums)

        low = 0
        high = n-1
        target = float("inf")

        while low <=high:
            mid = (low + high)//2
            target = min(target,nums[mid])

            if nums[mid]<= nums[high]:
                high = mid-1
            else:
                low = mid +1
        return target
        