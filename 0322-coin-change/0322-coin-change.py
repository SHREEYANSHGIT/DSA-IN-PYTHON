class Solution(object):

    def find(self, i, coins, amount, dp):

        if amount == 0:
            return 0

        if i < 0:
            return float("inf")

        if (i, amount) in dp:
            return dp[(i, amount)]

        pick = float("inf")

        if amount >= coins[i]:
            pick = 1 + self.find(
                i, coins, amount - coins[i], dp
            )

        notpick = self.find(
            i - 1, coins, amount, dp
        )

        dp[(i, amount)] = min(pick, notpick)

        return dp[(i, amount)]

    def coinChange(self, coins, amount):
        dp = {}

        ans = self.find(len(coins) - 1,coins,amount,dp)

        if ans == float("inf"):
            return -1

        return ans