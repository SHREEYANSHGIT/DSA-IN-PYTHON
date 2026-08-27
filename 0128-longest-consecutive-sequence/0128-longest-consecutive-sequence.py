class Solution(object):
    def longestConsecutive(self, nums):
        hashmap = {}
        maxi = 0
        for num in nums:
            hashmap[num] = hashmap.get(num , 0)+1
        
        for num in hashmap:
            if num - 1 not in hashmap:
                count = 1
                x = num
                while x +1 in hashmap:
                    x += 1
                    count +=1  
                maxi = max(count , maxi)
        
        return maxi

                