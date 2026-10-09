class Solution(object):
    def find(self, i, csum, candidates, target, path, ans):
        if csum == target:
            ans.append(path[:])
            return

        if i >= len(candidates) or csum > target:
            return

        # Pick the current candidate (reuse allowed)
        path.append(candidates[i])
        self.find(i, csum + candidates[i],
                  candidates, target, path, ans)

        # Backtrack
        path.pop()

        # Skip the current candidate
        self.find(i + 1, csum, candidates, target, path, ans)

    def combinationSum(self, candidates, target):
        ans = []
        self.find(0, 0, candidates, target, [], ans)
        return ans