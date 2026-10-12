class Solution(object):
    def find(self, i, csum, candidates, target, path, ans):
        if csum == target:
            ans.append(path[:])
            return

        if i >= len(candidates) or csum > target:
            return

        # Pick current candidate (only once)
        path.append(candidates[i])
        self.find(i + 1, csum + candidates[i],
                  candidates, target, path, ans)

        path.pop()

        # Skip duplicate values at this recursion level
        j = i + 1
        while j < len(candidates) and candidates[j] == candidates[i]:
            j += 1

        self.find(j, csum, candidates, target, path, ans)

    def combinationSum2(self, candidates, target):
        candidates.sort()
        ans = []
        self.find(0, 0, candidates, target, [], ans)
        return ans