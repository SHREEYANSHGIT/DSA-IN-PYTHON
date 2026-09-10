class Solution(object):
    def findSubstring(self, s, words):
        h1 = {}
        h2 = {}
        ans = []
        n = len(words[0])

        for i in range(len(words)):
            h1[words[i]] = h1.get(words[i], 0) + 1

        for start in range(n):
            h2 = {}
            l = start
            r = start

            while r + n <= len(s):
                word = s[r:r+n]
                h2[word] = h2.get(word, 0) + 1

                if r - l + n == n * len(words):
                    if h2 == h1:
                        ans.append(l)

                    h2[s[l:l+n]] -= 1
                    if h2[s[l:l+n]] == 0:
                        del h2[s[l:l+n]]
                    l += n

                r += n

        return ans