class Solution(object):
    def scoreOfParentheses(self, s):
        
        c = 0
        x = 0
        
        for i in range(len(s)):
            if s[i] == "(":
                x += 1

            elif s[i] == ")":
                x -=1
                if s[i-1] == "(":
                    c += 2**x
                
        return c


                