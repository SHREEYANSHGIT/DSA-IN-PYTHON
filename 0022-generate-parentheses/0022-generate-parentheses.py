class Solution(object):
    def find(self, n , left , right , curr ,ans):
        if left + right == 2*n:
            ans.append(curr)
            return 
        if right < left :
            self.find(n,left ,right+1 , curr + ")" ,ans)
        if left < n:
            self.find(n,left+1 ,right , curr + "(" ,ans)
    def generateParenthesis(self, n):
        curr = ""
        ans = []
        self.find(n,0 ,0 , curr ,ans)
        return ans

