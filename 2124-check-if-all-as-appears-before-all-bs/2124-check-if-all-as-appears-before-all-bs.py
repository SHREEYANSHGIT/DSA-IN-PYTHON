class Solution(object):
    def checkString(self, s):
        n = len(s)
        b = -1
        for i in range(n):
            if s[i] == "b":
                b = i
                break
        if b == -1:
            b = n+1
        for i in range(0,n):
            if s[i] == "a":
                if i > b:
                    return False
        
        return True