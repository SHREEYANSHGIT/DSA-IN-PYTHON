class Solution(object):
    def rob(self, nums):
        hashmap = {}

        def find(i):
            if i < 0:
                return 0

            if i in hashmap:
                return hashmap[i]

            chori = nums[i] + find(i - 2)
            nahi_chori = find(i - 1)

            ans = max(chori, nahi_chori)

            hashmap[i] = ans

            return ans

        return find(len(nums) - 1)