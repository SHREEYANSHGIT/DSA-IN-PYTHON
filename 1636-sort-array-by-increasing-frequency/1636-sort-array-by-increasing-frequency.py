class Solution(object):
    def frequencySort(self, nums):
        hm = {}

        for i in range(0,len(nums)):
            hm[nums[i]] = hm.get(nums[i],0) + 1
        
        heap = []
        ans = []
        for x , freq in hm.items():
            heapq.heappush(heap,(freq,-x))

        while heap:
            freq , nx = heapq.heappop(heap)
            nx = -nx

            for j in range(0,freq):
                ans.append(nx)
        
        return ans
                
            


        