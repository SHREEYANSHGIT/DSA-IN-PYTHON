class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        result = []
        
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = n-1
            needed = -(nums[i])

            while j<k:
                currsum = (nums[j]+ nums[k]) 
                if currsum== needed:
                    result.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                
                elif currsum < needed:
                    j = j+1
                else:
                    k = k-1

            

        return result
                    
                