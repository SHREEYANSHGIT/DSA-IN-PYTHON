class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        s = 0 

        while left < right:
            left = left >> 1
            right = right >> 1
            s+=1
        if right == left :
            right = right << s
        return right
        

        
        
