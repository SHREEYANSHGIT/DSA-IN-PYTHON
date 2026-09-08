class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        return self.atmost(nums, k) - self.atmost(nums, k - 1)
    
    def atmost(self,nums,k):
        l = 0
        r = 0
        hm = {}
        c = 0
        n = len(nums)

        while r < n:
            hm[nums[r]] = hm.get(nums[r],0) + 1

            while len(hm)>k :
                hm[nums[l]] -=1
                if hm[nums[l]] == 0:
                    del hm[nums[l]]
                l = l +1
            
            c += r-l+1 
            r = r+1
            
        return c

        