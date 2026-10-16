class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key = lambda x : x[0]) 
        previ = intervals[0][0]
        prevj = float("-inf")
        c = 0
        for i,j in intervals:
            if i < prevj:
                c +=1
                prevj = min(prevj, j)

            else:
                
                prevj = j 
        return c


