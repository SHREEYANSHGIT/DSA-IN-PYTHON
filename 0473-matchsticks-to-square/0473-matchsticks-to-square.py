class Solution(object):
    def find(self, i, matchsticks, check, target, tsum, sides):
        if sides == 3:
            return True

        if tsum == target:
            return self.find(0, matchsticks, check, target, 0, sides + 1)

        for j in range(i, len(matchsticks)):
            if check[j]:
                continue

            if tsum + matchsticks[j] > target:
                continue

            check[j] = True

            if self.find(
                j + 1, matchsticks, check,
                target, tsum + matchsticks[j], sides
            ):
                return True

            check[j] = False

        return False

    def makesquare(self, matchsticks):
        if len(matchsticks) < 4 or sum(matchsticks) % 4 != 0:
            return False

        target = sum(matchsticks) // 4

        if max(matchsticks) > target:
            return False

        matchsticks.sort(reverse=True)
        check = [False] * len(matchsticks)

        return self.find(0, matchsticks, check, target, 0, 0)