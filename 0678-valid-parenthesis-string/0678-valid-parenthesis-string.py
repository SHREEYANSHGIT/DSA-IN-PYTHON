class Solution(object):
    def checkValidString(self, s):
        st1 = []  # indices of '('
        st2 = []  # indices of '*'

        for i in range(len(s)):

            if s[i] == "(":
                st1.append(i)

            elif s[i] == "*":
                st2.append(i)

            else:  # ')'
                if st1:
                    st1.pop()
                elif st2:
                    st2.pop()
                else:
                    return False

        # Match remaining '(' with '*' that occur AFTER them
        while st1 and st2:
            if st1[-1] < st2[-1]:
                st1.pop()
                st2.pop()
            else:
                return False

        return len(st1) == 0