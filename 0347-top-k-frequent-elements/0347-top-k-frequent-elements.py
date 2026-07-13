import heapq

class Solution(object):
    def topKFrequent(self, nums, k):

        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num,0)+1
        
        heap = []
        for num,freq in hashmap.items():
            heapq.heappush(heap,(freq,num))
            if len(heap)>k:
                heapq.heappop(heap)
            
        ans = []

        while heap:
            e = heapq.heappop(heap)[1]
            ans.append(e)

        return ans