class Solution(object):
    def find(self,i,nums,tarr,ans,path):
        if len(nums) == len(path):
            ans.append(path[:])
            return
        
        for j in range(i,len(nums)):
            if tarr[j] == -1:
                tarr[j] = 0
                path.append(nums[j])
                self.find(0,nums,tarr,ans,path)
                path.pop()
                tarr[j] = -1
    
    def permute(self, nums):
        ans = []
        tarr = [-1]*len(nums)
        self.find(0,nums,tarr,ans,[])
        return ans 
        