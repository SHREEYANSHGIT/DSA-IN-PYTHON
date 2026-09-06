class Solution(object):
    def subarraysDivByK(self, nums, k):
        prefix = 0
        n = len(nums)
        hashmap = {0:1}
        c = 0 

        for i in range(n):
            prefix += nums[i]

            r = prefix % k
            if r in hashmap:
                c = c + hashmap[r]
            hashmap[r] = hashmap.get(r , 0)+1
        
        return c

             

