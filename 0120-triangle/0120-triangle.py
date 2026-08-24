#most optimal 
class Solution(object):

    def minimumTotal(self, triangle): 
        n = len(triangle)
        dp = [["x"] * len(triangle[i]) for i in range(n)]
        dp[-1] = triangle[-1][:]

        for i in range(n-2 , -1 , -1):
            for j in range(len(triangle[i])):
                dp[i][j] = triangle[i][j] + min(dp[i+1][j] , dp[i+1][j+1]) 

        return dp[0][0] 


# class Solution(object):

#     def find(self, i, j, triangle,dp):

#         if i == len(triangle) - 1:
#             return triangle[i][j]

#         if dp[i][j] != "x":
#             return dp[i][j]
#         left = self.find(i + 1, j, triangle,dp)
#         right = self.find(i + 1, j + 1, triangle,dp)

#         dp[i][j] = triangle[i][j] + min(left, right)

#         return dp[i][j]

#     def minimumTotal(self, triangle):

#         n = len(triangle)
#         dp = [["x"] * len(triangle[i]) for i in range(n)]
#         return self.find(0, 0, triangle,dp)


