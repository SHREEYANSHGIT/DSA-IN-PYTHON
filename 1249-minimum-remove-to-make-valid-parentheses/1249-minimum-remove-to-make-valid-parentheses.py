class Solution(object):
    def minRemoveToMakeValid(self, s):
        st = []
        remove = set()

        # Find invalid parentheses
        for i in range(len(s)):
            if s[i] == "(":
                st.append(i)

            elif s[i] == ")":
                if st:
                    st.pop()
                else:
                    remove.add(i)

        # Unmatched '(' are also invalid
        while st:
            remove.add(st.pop())

        # Build answer
        ans = ""

        for i in range(len(s)):
            if i not in remove:
                ans += s[i]

        return ans