import math

class Solution(object):
    def judgeSquareSum(self, c):
        root = int(math.sqrt(c))

        for a in range(root + 1):
            remaining = c - a * a

            b = int(math.sqrt(remaining))

            if b * b == remaining:
                return True

        return False