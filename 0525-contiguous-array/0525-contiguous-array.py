class Solution(object):
    def findMaxLength(self, nums):
        n = len(nums)
        zeros = 0
        ones = 0
        maxi = 0
        hashmap = {0:-1}
        diff = 0
        for i in range(n):
            if nums[i] == 0:
                zeros += 1
            else:
                ones += 1
            
            diff = zeros - ones

            if diff in hashmap:
                maxi = max(maxi, i - hashmap[diff])
            else : 
                hashmap[diff] = i
            
        return maxi 