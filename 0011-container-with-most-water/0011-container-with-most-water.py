class Solution(object):
    def maxArea(self, height):
        n = len(height)
        i = 0 
        j = n-1
        area = 0 
        ans = 0

        while i<j :
            ans = min(height[i],height[j])
            area = max(area , (ans * (j-i)) ) 

            if height[i] < height[j]:
                i = i+1
            else : 
                j = j-1
        
        return area 

        