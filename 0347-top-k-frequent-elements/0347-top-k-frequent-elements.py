class Solution(object):
    def topKFrequent(self, nums, k):

        # Step 1: Frequency Map
        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        # Step 2: Create Buckets
        bucket = [[] for _ in range(len(nums) + 1)]

        # Step 3: Fill Buckets
        for num, freq in hashmap.items():
            bucket[freq].append(num)

        # Step 4: Collect Answer
        ans = []

        for freq in range(len(bucket) - 1, 0, -1):
            for num in bucket[freq]:
                ans.append(num)

                if len(ans) == k:
                    return ans