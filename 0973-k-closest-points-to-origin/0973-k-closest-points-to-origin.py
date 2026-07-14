import heapq
class Solution(object):
    def kClosest(self, points, k):
        heap = []

        for i in range(0,len(points)):
            x = points[i][0]
            y = points[i][1]

            dis = x*x + y*y

            heapq.heappush(heap,(-dis,points[i]))

            if len(heap)>k:
                heapq.heappop(heap)



        ans = []

        while heap:
            ans.append(heapq.heappop(heap)[1])
        
        return ans