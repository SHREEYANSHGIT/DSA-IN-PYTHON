class Solution(object):

    def minCostClimbingStairs(self, cost):
        cost.append(0)
        n = len(cost)

        last2 = cost[0]
        last1 = cost[1]
        curr = 0

        for i in range(2, n):
            curr = cost[i] + min(last1, last2)
            last2 = last1
            last1 = curr

        return curr