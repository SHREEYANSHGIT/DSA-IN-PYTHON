class Solution(object):
    def findComplement(self, num):
        length = num.bit_length()
        mask = (1 << length) - 1

        return num ^ mask