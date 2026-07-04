class Solution(object):
    def subarraySum(self, nums, k):
        # n = len(nums)
        # prefixsummap ={}
        # count =0
        # currsum = 0
        # for i in range(0,n):
        #     currsum += nums[i]
        #     if currsum == k:
        #         count+=1

        #     if currsum-k in prefixsummap:
        #         count +=  prefixsummap[currsum - k]
            
        #     prefixsummap[currsum] = prefixsummap.get(currsum,0)+1
        
        # return count

        n = len(nums)
        hashmap={0:1}
        csum = 0
        count = 0


        for i in range(0,n):
            csum += nums[i]

            if csum-k in hashmap:
                count += hashmap[csum-k]
            
            hashmap[csum] = hashmap.get(csum , 0)+1
        
        return count
        



        



        