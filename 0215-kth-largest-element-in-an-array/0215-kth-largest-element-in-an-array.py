import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        ans = []
        n = len(nums)
        for i in range(0,k):
            heapq.heappush(ans,nums[i])
        
        for i in range(k,n):
            if nums[i]>ans[0]:
                heapq.heappop(ans)
                heapq.heappush(ans,nums[i])

        return ans[0]


