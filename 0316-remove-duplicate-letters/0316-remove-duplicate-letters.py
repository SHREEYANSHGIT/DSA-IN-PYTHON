class Solution(object):
    def removeDuplicateLetters(self, s):
        st = []
        n = len(s)
        hashmap = {}
        for i in range(n):
            hashmap[s[i]] = i

        for i in range(n):
            while st and st[-1] >= s[i] and (hashmap[st[-1]] > i) and s[i] not in st:
                st.pop()
            if s[i] not in st:
                st.append(s[i])
        
        return ''.join(st)
        