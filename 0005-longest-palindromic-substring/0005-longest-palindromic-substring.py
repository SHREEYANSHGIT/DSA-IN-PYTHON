class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)

        if n == 0:
            return ""

        ans = s[0]
        le = 1

        for i in range(n):

            # Odd length palindrome
            l, r = i, i

            while l >= 0 and r < n and s[l] == s[r]:

                if (r - l + 1) > le:
                    le = r - l + 1
                    ans = s[l:r+1]

                l -= 1
                r += 1

            # Even length palindrome
            l, r = i, i + 1

            while l >= 0 and r < n and s[l] == s[r]:

                if (r - l + 1) > le:
                    le = r - l + 1
                    ans = s[l:r+1]

                l -= 1
                r += 1

        return ans