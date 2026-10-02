import math

class Solution(object):
    def judgeSquareSum(self, c):
        root = int(math.sqrt(c))

        l = 0
        r = root

        while l<=r:
            t = l*l + r*r
            if c == t:
                return True
            if t < c:
                l = l+1
            else:
                r = r-1
        return False