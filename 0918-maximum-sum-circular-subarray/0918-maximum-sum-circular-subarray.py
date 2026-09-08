class Solution(object):
    def maxSubarraySumCircular(self, nums):
        maxi =float("-inf")
        mini =float("inf")
        c1 = 0
        c2 = 0
        n = len(nums)
        for i in range(0,n):
            c1 += nums[i]
            maxi = max(c1,maxi) 
            if c1 < 0 :
                c1 = 0
            
        if maxi < 0:
            return maxi
            
        
        for j in range(0,n):
            c2  += nums[j]
            mini = min(mini,c2)
            if c2 > 0:
                c2 = 0
        

        return max((sum(nums) - mini) , maxi)
            
        