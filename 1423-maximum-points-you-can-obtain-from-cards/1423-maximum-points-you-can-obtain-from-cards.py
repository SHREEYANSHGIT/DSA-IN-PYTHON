class Solution(object):
    def maxScore(self, cardPoints, k):
        n = len(cardPoints)
        if n == k:
            return sum(cardPoints)

        leftsum,rightsum = 0,0
        for i in range(0,k):
            leftsum += cardPoints[i]
            maxi = leftsum
        left = k-1 
        right = n-1
        while left >= 0:
            rightsum += cardPoints[right]
            leftsum -= cardPoints[left]
            maxi = max(maxi , leftsum + rightsum)
            left -=1
            right -=1

        return maxi  


