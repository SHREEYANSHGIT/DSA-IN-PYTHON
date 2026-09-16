class Solution(object):
    def removeKdigits(self, num, k): 
        n = len(num)
        st = []

        for i in range(n):
            while st and k >0 and  st[-1] > num[i]:
                st.pop()
                k -=1
            
            st.append(num[i])

        while st and k > 0:
            st.pop()
            k -= 1

        ans = ''.join(st).lstrip('0')

        if ans == "":
            return "0"

        return ans
            
            
