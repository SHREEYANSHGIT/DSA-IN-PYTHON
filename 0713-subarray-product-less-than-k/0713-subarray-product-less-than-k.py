
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        # result = math.prod(nums)
        n = len(nums)
        # if result < k :
        #     return n
        
        l = 0
        r = 0
        c = 0
        p = 1
        while r < n:
            p *= nums[r]

            while p >= k and l < n:
                p //= nums[l]
                l = l+1
            
            if p < k :
                c  = c + (r - l + 1)
            r = r+1
        
        return c 


        