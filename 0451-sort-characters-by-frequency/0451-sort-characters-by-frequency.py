class Solution(object):
    def frequencySort(self, s):
        hm = {}
        ans = ""

        for ch in s:
            hm[ch] = hm.get(ch, 0) + 1

        bucket = [[] for _ in range(len(s) + 1)]
        n = len(bucket)

        for ch, freq in hm.items():
            bucket[freq].append(ch)

        for i in range(len(s),0,-1):
            for ch in bucket[i]:
                ans += ch * i
        return ans