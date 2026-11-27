
class Solution(object):
    def maximumSaleItems(self, items, budget):
        n = len(items)

        # Calculate free copies for each item
        free = [0] * n

        for i in range(n):
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    free[i] += 1

        # Group items by price
        groups = {}

        for i in range(n):
            factor, price = items[i]
            groups.setdefault(price, []).append(free[i] + 1)

        NEG = -10**9

        # dp[c] = maximum selected + free items at exact cost c
        dp = [NEG] * (budget + 1)
        dp[0] = 0

        ans = 0

        # Process prices from highest to lowest
        for price in sorted(groups, reverse=True):

            # Must select at least one item of current price
            current = [NEG] * (budget + 1)

            for value in groups[price]:

                for c in range(budget, price - 1, -1):

                    if dp[c - price] != NEG:
                        current[c] = max(
                            current[c],
                            dp[c - price] + value
                        )

                    dp[c] = max(
                        dp[c],
                        dp[c - price] + value
                    )

            # Calculate maximum total including extra copies
            for c in range(budget + 1):
                if current[c] != NEG:
                    ans = max(
                        ans,
                        current[c] + (budget - c) // price
                    )

        return ans
