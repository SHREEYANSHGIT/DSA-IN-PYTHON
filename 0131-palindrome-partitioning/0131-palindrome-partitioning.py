class Solution(object):
    def p(self,s):
        n = len(s)
        l = 0
        r = n -1
        while r>=l:
            if s[l] == s[r]:
                l +=1
                r -=1
            else:
                return False

        return True 
    def find(self,i,s,ans,path):
        if i >= len(s):
            ans.append(path[:])
            return
        for j in range(i,len(s)):
            x = s[i:j+1]
            if self.p(x):
                path.append(x)
                self.find(j+1,s,ans,path)
                path.pop()


    def partition(self, s):
        ans = []
        self.find(0,s,ans,[])
        return ans
        