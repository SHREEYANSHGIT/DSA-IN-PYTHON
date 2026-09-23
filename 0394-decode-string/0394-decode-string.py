class Solution(object):
    def decodeString(self, s):
        st = []

        for ch in s:

            if ch != "]":
                st.append(ch)

            else:
                temp = ""

                while st and st[-1] != "[":
                    temp = st.pop() + temp

                st.pop()

                num = ""

                while st and st[-1].isdigit():
                    num = st.pop() + num

                num = int(num)
                temp = temp * num

                st.append(temp)

        return "".join(st)