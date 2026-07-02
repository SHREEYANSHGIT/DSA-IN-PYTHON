class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        l = 0
        r = 0
        maxi = 0
        mydict={}

        while r<n :
            if s[r] in mydict:
                l = max(l,mydict[s[r]]+1)

            maxi = max(maxi , r-l+1)

            mydict[s[r]] = r

            r +=1
        
        return maxi
            

