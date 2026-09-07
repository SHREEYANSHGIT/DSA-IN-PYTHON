class Solution(object):
    def checkSubarraySum(self, nums, k):
        hashmap = {0: -1}
        prefix = 0
        n = len(nums)
        
        for i in range(0,n):
            prefix += nums[i] 
            remainder = prefix % k
            if remainder in hashmap:
                if i - hashmap[remainder]  >=2:
                    return True 
            else:
                hashmap[remainder] = i
        
        return False
            
        