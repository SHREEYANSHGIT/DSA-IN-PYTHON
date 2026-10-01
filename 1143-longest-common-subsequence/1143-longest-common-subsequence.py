class Solution(object):
    def find(self,i , j , text1 , text2 ,dp):
        if len(text1) == i or len(text2) == j:
            return 0
        
        if (i, j) in dp:
            return dp[(i, j)]

        if text1[i] == text2[j]:
            dp[(i, j)] = 1 + self.find(i+1 , j+1 , text1 , text2 ,dp)

        else:
            left = self.find(i+1 , j , text1 , text2 ,dp)
            right = self.find(i , j+1 , text1 , text2 ,dp)
            dp[(i, j)] = max(left,right)

        return dp[(i, j)]


    def longestCommonSubsequence(self, text1, text2):
        dp = {}
        ans = self.find(0 , 0 , text1 , text2 ,dp)
        return ans

