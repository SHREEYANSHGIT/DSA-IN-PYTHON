class Solution(object):
    def findContentChildren(self, g, s):
        g = sorted(g)
        s = sorted(s)
        n = len(g)
        m = len(s)
        i,j = 0,0
        count = 0
        while i<n and j<m:
            if s[j] >= g[i]:
                count+=1
                i+=1
                j+=1
            else:
                j+=1
        
        return count