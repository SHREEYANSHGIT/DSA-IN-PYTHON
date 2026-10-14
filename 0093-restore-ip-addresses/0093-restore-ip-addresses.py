class Solution(object):
    def find(self,i,path,ans,s):
        if len(path) == 4:
            if i == len(s):
                ans.append(".".join(path))
            return
        
        for j in range(i,min(i+3,len(s))):
            x = s[i:j+1]
            if len(x) > 1 and x[0] == "0":
                continue
            if int(x) > 255:
                continue
            else:
                path.append(x)
            self.find(j+1,path,ans,s)
            path.pop()

    def restoreIpAddresses(self, s):
        ans = []
        self.find(0,[],ans,s)
        return ans 