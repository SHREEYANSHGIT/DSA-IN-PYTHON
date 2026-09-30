class Solution(object):
    def increasingTriplet(self, nums):
        m = float("inf")
        n = float("inf")

        
        for i in range(len(nums)):
            if nums[i] > n and n > m:
                return True
            m = min(nums[i],m)
            if nums[i] > m :
                n = nums[i]
        
        return False
            
                
