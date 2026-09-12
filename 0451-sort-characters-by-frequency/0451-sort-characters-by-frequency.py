class Solution(object):
    def frequencySort(self, s):
        hm = {}
        ans = ""

        for ch in s:
            hm[ch] = hm.get(ch, 0) + 1

        sorted_hm = sorted(hm.items(), key=lambda x: x[1], reverse=True)

        for ch, freq in sorted_hm:
            ans += ch * freq

        return ans