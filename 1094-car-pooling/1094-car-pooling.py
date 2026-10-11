class Solution(object):
    def carPooling(self, trips, capacity):
        my_heap = []

        for i in trips:
            x ,y , z = i
            heapq.heappush(my_heap, (y,x))
            heapq.heappush(my_heap, (z,-x))

        c = 0
        while my_heap:
            l , m = heapq.heappop(my_heap)
            c += m
            if c > capacity:
                return False
        
        return True 
            

            
            



                

            
            


        