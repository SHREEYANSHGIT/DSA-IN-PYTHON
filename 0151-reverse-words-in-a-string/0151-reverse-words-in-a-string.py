class Solution(object):
    def reverseWords(self, s):
        n = len(s)
        r = n - 1
        ans = []

        while r >= 0:

            # Skip spaces
            while r >= 0 and s[r] == " ":
                r -= 1

            if r < 0:
                break

            # Find beginning of word
            l = r

            while l >= 0 and s[l] != " ":
                l -= 1

            ans.append(s[l + 1:r + 1])

            r = l - 1

        return " ".join(ans)