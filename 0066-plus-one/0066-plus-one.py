class Solution(object):
    def plusOne(self, digits):

        n = len(digits)
        number = 0
        for i in range(n):
            number *= 10
            number += digits[i] 

        number += 1
        for k in range(n-1 , -1 , -1):
            x = number % 10
            digits[k] = x

            number = number // 10

        if  number != 0 :
            return [number] + digits
        return digits 
