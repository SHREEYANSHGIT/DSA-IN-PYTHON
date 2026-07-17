class MedianFinder(object):

    def __init__(self):
        self.minheap = []
        self.maxheap = []
        

    def addNum(self, num):
        heapq.heappush(self.maxheap,-num)
        value = heapq.heappop(self.maxheap)
        heapq.heappush(self.minheap,-value)
        
        if len(self.minheap) > len(self.maxheap)+1:
            value = heapq.heappop(self.minheap) 
            heapq.heappush(self.maxheap,-value)


    def findMedian(self):
        if (len(self.minheap) + len(self.maxheap)) % 2 == 0:
            return (self.minheap[0] + (-self.maxheap[0])) / 2.0

        else :
            return self.minheap[0]

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()