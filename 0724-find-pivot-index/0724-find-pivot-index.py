class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        prefixsum = [0]*n
        sufixsum = [0]*n

        for i in range(1,n):
            prefixsum[i] = prefixsum[i-1] + nums[i-1]
        
        for j in range(n-2,-1,-1):
            sufixsum[j] = sufixsum[j+1] + nums[j+1]
        
        for k in range(n) :
            if sufixsum[k]==prefixsum[k]:
                return k

        return -1