class Solution(object):
    def checkInclusion(self, s1, s2):
        s1map = {}
        s2map = {}
        n = len(s1)

        # Frequency of s1
        for i in range(n):
            s1map[s1[i]] = s1map.get(s1[i], 0) + 1

        l = 0
        r = 0

        while r < len(s2):
            while r - l + 1 < n and r < len(s2):
                s2map[s2[r]] = s2map.get(s2[r], 0) + 1
                r += 1

            if r < len(s2):
                s2map[s2[r]] = s2map.get(s2[r], 0) + 1

            if s2map == s1map:
                return True

            s2map[s2[l]] -= 1

            if s2map[s2[l]] == 0:
                del s2map[s2[l]]

            l += 1
            r += 1

        return False