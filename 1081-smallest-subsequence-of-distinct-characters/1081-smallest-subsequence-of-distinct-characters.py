
class Solution(object):
    def smallestSubsequence(self, s):
        freq = {}
        st = []
        seen = set()

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for ch in s:
            freq[ch] -= 1

            if ch in seen:
                continue

            while st and st[-1] > ch and freq[st[-1]] > 0:
                seen.remove(st.pop())

            st.append(ch)
            seen.add(ch)

        return "".join(st)
