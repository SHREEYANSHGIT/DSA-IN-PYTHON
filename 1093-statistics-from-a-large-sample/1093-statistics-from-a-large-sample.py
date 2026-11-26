
class Solution(object):
    def sampleStats(self, count):
        total = 0
        s = 0
        mini = -1
        maxi = -1
        mode = 0
        max_freq = 0

        for i in range(256):
            if count[i] > 0:
                if mini == -1:
                    mini = i

                maxi = i

                total += count[i]
                s += i * count[i]

                if count[i] > max_freq:
                    max_freq = count[i]
                    mode = i

        # Median
        mid1 = (total + 1) // 2
        mid2 = (total + 2) // 2

        curr = 0
        a = 0
        b = 0

        for i in range(256):
            curr += count[i]

            if curr >= mid1 and a == 0:
                a = i

            if curr >= mid2:
                b = i
                break

        mean = float(s) / total
        median = (a + b) / 2.0

        return [float(mini), float(maxi), mean, median, float(mode)]
