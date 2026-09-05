class Solution(object):
    def characterReplacement(self, s, k):
        hashmap = {}
        l = 0
        r = 0
        maxi = 0
        max_freq = 0

        while r < len(s):

            # Add current character to frequency map
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1

            # Highest frequency character in current window
            max_freq = max(max_freq, hashmap[s[r]])

            # Number of replacements required
            window_size = r - l + 1
            replacements = window_size - max_freq

            # Window is invalid
            if replacements > k:
                hashmap[s[l]] -= 1
                l += 1

            # Current valid window length
            maxi = max(maxi, r - l + 1)

            r += 1

        return maxi