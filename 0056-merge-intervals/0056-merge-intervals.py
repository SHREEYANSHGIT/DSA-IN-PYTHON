
class Solution(object):
    def merge(self, intervals):
        sorted_intervals = sorted(intervals, key=lambda x: x[0])

        last_i = sorted_intervals[0][0]
        last_j = sorted_intervals[0][1]

        ans = []

        for v in range(1, len(sorted_intervals)):
            i = sorted_intervals[v][0]
            j = sorted_intervals[v][1]

            if last_j >= i:
                s = min(last_i, i)
                e = max(last_j, j)
            else:
                ans.append([last_i, last_j])
                s = i
                e = j

            last_i = s
            last_j = e

        ans.append([last_i, last_j])

        return ans
