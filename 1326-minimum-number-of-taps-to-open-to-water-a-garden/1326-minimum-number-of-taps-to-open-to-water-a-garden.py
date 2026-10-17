class Solution(object):
    def minTaps(self, n, ranges):
        startEnd = [0] * (n + 1)

        for i in range(len(ranges)):
            start = max(0, i - ranges[i])
            end = min(n, i + ranges[i])

            startEnd[start] = max(startEnd[start], end)

        taps = 0
        currEnd = 0
        maxEnd = 0

        for i in range(n + 1):
            if i > maxEnd:
                return -1

            if i > currEnd:
                taps += 1
                currEnd = maxEnd

            maxEnd = max(maxEnd, startEnd[i])

        return taps