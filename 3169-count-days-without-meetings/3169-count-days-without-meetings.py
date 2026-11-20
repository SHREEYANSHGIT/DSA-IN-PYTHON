class Solution(object):
    def countDays(self, days, meetings):
        meetings = sorted(meetings,key =lambda x : x[0])
        n = len(meetings)
        c = 0
        s = meetings[0][0]
        e = meetings[0][1]
        for i in range(1,n):
            a = meetings[i][0]
            b = meetings[i][1]
            if a > e:
                c += e - s + 1
                s = a
                e = b
            else:
                e = max(b,e)
                s = min(a,s)
            
        c += e-s+1

        return days - c

                