class Solution(object):
    def climbStairs(self, n):
        hashmap = {}

        def find(n , hashmap):
            if n == 1:
                return 1
            if n == 2 :
                return 2

            if n in hashmap:
                return hashmap[n]
            
            ans = find(n-1,hashmap) + find(n-2,hashmap)
            hashmap[n] = ans
            return ans 
        return find(n , hashmap)

            
