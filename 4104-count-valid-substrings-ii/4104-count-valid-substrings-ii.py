class Solution(object):
    def countValidSubstrings(self, s):
        la = -1
        lab = -1
        labc = -1
        c = 0
        l = 0
        for r in range(len(s)):
            if s[r] == "a":
                la = r
            elif s[r] == "b":
                if la != -1:
                    lab = max(la,lab)
            elif s[r] == "c":
                if lab != -1:
                    labc = max(lab,labc)
                    l = labc + 1
            
            c += r - l + 1
        return c



