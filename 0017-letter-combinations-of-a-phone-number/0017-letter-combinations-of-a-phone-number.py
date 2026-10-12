
class Solution(object):
    def find(self, i, hm, path, ans, digits):
        if i >= len(digits):
            ans.append("".join(path))
            return

        x = hm[digits[i]]

        for ch in x:
            path.append(ch)
            self.find(i + 1, hm, path , ans, digits)
            path.pop()

    def letterCombinations(self, digits):
        if not digits:
            return []

        hm = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        ans = []
        self.find(0, hm, [], ans, digits)
        return ans
