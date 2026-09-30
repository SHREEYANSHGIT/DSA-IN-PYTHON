class Solution(object):
    def removeStars(self, s):
        ans = ""
        c = 0
        n = len(s)
        for i in range(n-1 , -1 ,-1):
            if s[i] !="*" and c ==0:
                ans = s[i] + ans
            elif s[i]=="*":
                c = c+1
            elif s[i] !="*" and c>0:
                c =c-1

        return ans  
            