class Solution(object):
    def partitionLabels(self, s):
        hashmap = {}
        ans = []
        for i in range(len(s)):
            hashmap[s[i]] = i
        k = 0
        x = 0
        for j in range(len(s)):
            x = max( x,  hashmap[s[j]])
            
            if x == j:
                ans.append(j - k+1)
                k = j+1
        
        return ans 

                

        


        