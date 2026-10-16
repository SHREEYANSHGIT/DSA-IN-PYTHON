class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key = lambda x : x[0]) 
        previ = intervals[0][0]
        prevj = float("-inf")
        c = 0
        for i,j in intervals:
            if i < prevj:
                c +=1
                if j < prevj:
                    prevj = j
                    previ = i
                if j == prevj :
                    if i > previ:
                        previ = i 

            else:
                previ = i
                prevj = j 
        return c


