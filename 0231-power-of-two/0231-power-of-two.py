class Solution(object):
    def isPowerOfTwo(self, n):
        x = 1

        if n <= 0:
            return False

        while x <= n:
            if x == n :
                return True
            
            x = x * 2

        return False 