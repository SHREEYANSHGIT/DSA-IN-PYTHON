class Solution(object):
    def scoreOfParentheses(self, s):
        st = []
        c = 0
        
        for i in range(len(s)):
            if s[i] == "(":
                st.append(c)
                c = 0
            
            elif s[i] == ")":
                if s[i-1] == "(":
                    c = st[-1] + 1
                else:
                    c = st[-1] + (2*c)
                st.pop()
        
        return c


                