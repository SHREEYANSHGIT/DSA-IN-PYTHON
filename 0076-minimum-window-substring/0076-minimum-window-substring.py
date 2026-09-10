class Solution(object):
    def minWindow(self, s, t):
        h1 = {}
        h2 = {}
        have = 0
        mini = float("inf")
        ans = ""
        for i in range(len(t)):
            h1[t[i]] = h1.get(t[i] , 0)+1
        r , l = 0 , 0
        while r < len(s):
            h2[s[r]] = h2.get(s[r] , 0)+1
            if s[r] in h1:
                if h1[s[r]] == h2[s[r]]:
                    have +=1 
            
            while have == len(h1) :
                if r-l+1 < mini:
                    mini = min(mini , r-l+1)
                    ans = s[l:r+1]
                h2[s[l]] -=1
                if s[l] in h1:
                    if h2[s[l]] < h1[s[l]]:
                        have -= 1
                l=l+1
            
            r =r+1
        
        return ans


                
