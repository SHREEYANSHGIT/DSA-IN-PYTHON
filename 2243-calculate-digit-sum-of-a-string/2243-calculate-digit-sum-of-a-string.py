class Solution(object):
    def find(self, arr, k):
        ans = []
        x = 0
        a = 0
        for i in range(len(arr)):
            x += 1
            a += int(arr[i])
            if x == k:
                ans.append(a)
                a = 0
                x = 0
        if x > 0:
            ans.append(a)
        return ans

    def digitSum(self, s, k):
        arr = list(s)

        while len(arr) > k:
            arr = self.find(arr, k)
            
            arr = list("".join(map(str, arr)))

        return "".join(arr)