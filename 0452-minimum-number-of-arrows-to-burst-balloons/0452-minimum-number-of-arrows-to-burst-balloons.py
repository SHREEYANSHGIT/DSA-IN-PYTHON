class Solution(object):
    def findMinArrowShots(self, points):
        points.sort(key= lambda x:x[0])
        if len(points) == 1:
            return 1
        pi = points[0][0]
        pj = points[0][1]
        ans = 1
        for i , j in points:
            if i <= pj:
                pi = max(i,pi)
                pj = min(j,pj)
            else:
                ans +=1
                pi = i
                pj = j
        
        return ans