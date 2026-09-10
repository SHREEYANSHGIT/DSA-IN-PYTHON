class Solution(object):
    def findAnagrams(self, s, p):
        shm = {}
        phm = {}
        ans = []
        l = 0
        r = 0
        n = len(p)

        if len(s) < len(p):
            return ans

        for i in range(n):
            phm[p[i]] = phm.get(p[i], 0) + 1

        while r < len(s):

            while r - l + 1 < n:
                shm[s[r]] = shm.get(s[r], 0) + 1
                r += 1

            shm[s[r]] = shm.get(s[r], 0) + 1

            if shm == phm:
                ans.append(l)

            shm[s[l]] -= 1

            if shm[s[l]] == 0:
                del shm[s[l]]

            l += 1
            r += 1

        return ans