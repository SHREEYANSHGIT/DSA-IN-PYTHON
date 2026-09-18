class Solution(object):
    def minAddToMakeValid(self, s):
        st = []

        n = len(s)

        for i in range(n):
            if not st and s[i] == ")":
                st.append(s[i])
                continue
            elif st and st[-1] == ")" and s[i] == ")":
                st.append(s[i])
                continue
            elif st and st[-1] == "(" and s[i] == ")": 
                st.pop()
                continue
            else:
                st.append(s[i])
        
        return len(st)
            

        