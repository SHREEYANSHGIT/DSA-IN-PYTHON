class Solution(object):
    def find(self,i,nums,path,ans):
        
        if i >= len(nums):
            ans.append(path[:])
            return 
            
        path.append(nums[i])
        
        
        self.find(i+1,nums,path,ans)
        path.pop()
        self.find(i+1,nums,path,ans)

        
    def subsets(self, nums):
        ans = []
        self.find(0,nums,[],ans)
        return ans

        