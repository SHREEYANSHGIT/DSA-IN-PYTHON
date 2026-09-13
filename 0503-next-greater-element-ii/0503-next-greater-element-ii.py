class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        st = []
        ans = [-1]*n
        for j in range((n+n-2),-1,-1):
            i = j%n

            while st and nums[st[-1]] <= nums[i] :
                st.pop()
            
            if j<n and st:
                ans[i] = nums[st[-1]]
            st.append(i)
        
        return ans

            

        