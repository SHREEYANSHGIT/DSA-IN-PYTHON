class Solution(object):
    def minEatingSpeed(self, piles, h):
        l = 1 
        r = max(piles)
        
        while l < r:
            mid = (r + l)//2
            s = 0
            for i in range(len(piles)):
                s +=  (piles[i] + mid - 1) // mid
            
            if s > h :
                l = mid + 1
            
            else:
                r = mid 
        
        return l
